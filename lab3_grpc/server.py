import grpc
from concurrent import futures
import time
import traceback

from proto import vocabulary_pb2
from proto import vocabulary_pb2_grpc

from vocabulary.vocabulary_service import VocabularyService
from word.word_service import WordService
from vocabulary.vocabulary_service import VocabularyFilters
from word.word_service import WordFilters

vocabulary = VocabularyService()
word = WordService(vocabulary)


def word_mapper(item) -> vocabulary_pb2.Word:
    w = vocabulary_pb2.Word()
    w.id = str(item.word_id)
    w.vocabulary_id = str(item.vocabulary_id)
    w.word_from_language = item.word_from_language
    w.word_to_language = item.word_to_language
    w.description = item.description
    return w


def vocabualary_mapper(vocab) -> vocabulary_pb2.Vocabulary:
    v = vocabulary_pb2.Vocabulary()
    v.id = str(vocab.vocab_id)
    v.name = vocab.vocab_name
    v.owner_id = str(vocab.owner_id)
    v.students_count = vocab.students_count
    v.language_to = vocab.language_to
    v.language_from = vocab.language_from
    for item in vocab.word_list:
        v.word_list.append(word_mapper(item))
    return v


class VocabularyControllerService(vocabulary_pb2_grpc.VocabularyControllerServicer):

    def CreateOrUpdateVocabulary(self, request, context):
        try:
            if request.id:
                result = vocabulary.update_vocabulary(request.id, request)
            else:
                result = vocabulary.create_vocabulary(request)
        except Exception as error:
            traceback.print_exc()  # prints full error to server terminal
            context.abort(grpc.StatusCode.INTERNAL, str(error))
        return vocabualary_mapper(result)

    def GetVocabularies(self, request, context):
        filters = VocabularyFilters(
            owner_id=request.owner_id,
            language_to=request.language_to,
            language_from=request.language_from,
        )

        try:
            result = vocabulary.get_vocabularies(filters, page=request.offset, size=request.limit)
        except ValueError as error:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(error))
        for vocab in result.content:
            yield vocabualary_mapper(vocab)

    def GetVocabulary(self, request, context):
        try:
            result = vocabulary.get_vocabulary(request.id)
        except ValueError as error:
            context.abort(grpc.StatusCode.NOT_FOUND, str(error))
        return vocabualary_mapper(result)


class WordControllerService(vocabulary_pb2_grpc.WordControllerServicer):

    def CreateOrUpdateWord(self, request, context):
        try:
            if request.id:
                result = word.update_word(request.vocabulary_id, request.id, request)
            else:
                result = word.create_word(request.vocabulary_id, request)
        except ValueError as error:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(error))
        except KeyError as error:
            context.abort(grpc.StatusCode.NOT_FOUND, str(error))
        return word_mapper(result)
    
    def CreateWords(self, request, context):
        count = 0
        seen = set()

        for word_request in request:
            key = (word_request.vocabulary_id, word_request.word_from_language, word_request.word_to_language)
            if key in seen:
                continue
            seen.add(key)
            try:
                word.create_word(word_request.vocabulary_id, word_request)
            except ValueError as error:
                context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(error))
            count += 1

        return vocabulary_pb2.WordsCreationResponse(word_number=count)


    def GetWords(self, request, context):
        try:
            result = word.get_words(vocab_id=request.vocabulary_id, page=request.offset, size=request.limit)
        except ValueError as error:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(error))
        for w in result.content:
            yield word_mapper(w)

    def GetWord(self, request, context):
        try:
            result = word.get_word(request.vocabulary_id, request.id)
        except ValueError as error:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(error))
        except KeyError as error:
            context.abort(grpc.StatusCode.NOT_FOUND, str(error))
        return word_mapper(result)
        


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

vocabulary_pb2_grpc.add_VocabularyControllerServicer_to_server(
    VocabularyControllerService(), server)
vocabulary_pb2_grpc.add_WordControllerServicer_to_server(
    WordControllerService(), server)

print('Starting server. Listening on port 50052.')
server.add_insecure_port('[::]:50052')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
