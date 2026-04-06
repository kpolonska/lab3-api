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


def generate_words(vocab_id):
    words = [
        vocabulary_pb2.Word(vocabulary_id=vocab_id, word_from_language='apple', word_to_language='яблуко'),
        vocabulary_pb2.Word(vocabulary_id=vocab_id, word_from_language='cat', word_to_language='кіт'),
    ]

    for w in words:
        yield w  

response = word_stub.CreateWords(generate_words(vocab.id))
print('Created:', response.word_number)

for w in word_stub.GetWords(vocabulary_pb2.WordFilters(vocabulary_id=vocab.id, limit=10, offset=1)):
    print(w.id, w.word_from_language, w.word_to_language)