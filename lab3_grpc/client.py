import grpc
import uuid

from proto import vocabulary_pb2
from proto import vocabulary_pb2_grpc


channel = grpc.insecure_channel('localhost:50052')
vocab_stub = vocabulary_pb2_grpc.VocabularyControllerStub(channel)
word_stub = vocabulary_pb2_grpc.WordControllerStub(channel)


vocab = vocab_stub.CreateOrUpdateVocabulary(
    vocabulary_pb2.Vocabulary(
        name='some-vocabualry',
        owner_id='user-1',
        language_from='en',
        language_to='uk'
    ),
    timeout = 5
)
print('Created vocab:', vocab.id)
print('Name:', vocab.name)
print('Owner:', vocab.owner_id)


def word_stream(vocab_id):
    words = [
        vocabulary_pb2.Word(vocabulary_id=vocab_id, word_from_language='apple', word_to_language='яблуко'),
        vocabulary_pb2.Word(vocabulary_id=vocab_id, word_from_language='cat', word_to_language='кіт'),
    ]

    for w in words:
        yield w  

response = word_stub.CreateWords(word_stream(vocab.id))
print('Created:', response.word_number)

word_id = ''
for w in word_stub.GetWords(vocabulary_pb2.WordFilters(vocabulary_id=vocab.id, limit=10, offset=1)):
    word_id = w.id
    print(w.id, w.word_from_language, w.word_to_language)


print('Get one vocabulary:')
fetched_vocab = vocab_stub.GetVocabulary(vocabulary_pb2.VocabularyRequest(id=vocab.id), timeout=5)
print('Vocabulary:', fetched_vocab.id, fetched_vocab.name)


print('Get one word')
fetched_word = word_stub.GetWord(vocabulary_pb2.WordRequest(vocabulary_id=vocab.id, id=word_id),timeout=5)
print('Word:', fetched_word.id, fetched_word.word_from_language)


print('Update a word.')
updated = word_stub.CreateOrUpdateWord(
    vocabulary_pb2.Word(
        id=word_id,
        vocabulary_id=vocab.id,
        word_from_language='apple pie',
        word_to_language='яблучний пиріг',
        description='A dessert'
    ), timeout=5)
print('Updated:', updated.id, updated.word_from_language)


print('Should return validation error:')
try:
    vocab_stub.CreateOrUpdateVocabulary(
        vocabulary_pb2.Vocabulary(name='', owner_id='user-1', language_from='en', language_to='uk'),
        timeout=5
    )
except Exception as e:
    print('Validation error:', e.code(), e.details())


print('Should return not found error:')
try:
    word_stub.GetWord(
        vocabulary_pb2.WordRequest(vocabulary_id=vocab.id, id='non-existent-id'),
        timeout=5
    )
except Exception as e:
    print('Not found error:', e.code(), e.details())