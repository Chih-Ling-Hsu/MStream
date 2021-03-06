from .DocumentSet import DocumentSet
from .Model import Model
import os

class MStream:

    def __init__(self, K, MaxBatch, AllBatchNum, alpha, beta, iterNum, sampleNum, dataDir, dataset, timefil, wordsInTopicNum):
        self.K = K
        self.MaxBatch = MaxBatch
        self.AllBatchNum = AllBatchNum
        self.alpha = alpha
        self.beta = beta
        self.iterNum = iterNum
        self.dataDir = dataDir
        self.dataset = dataset
        self.timefil = timefil
        self.sampleNum = sampleNum
        self.wordsInTopicNum = wordsInTopicNum
        self.wordList = []
        self.wordToIdMap = {}

    def getDocuments(self):
        self.documentSet = DocumentSet(os.path.join(self.dataDir, self.dataset), self.wordToIdMap, self.wordList)
        self.V = self.wordToIdMap.__len__()

    def runMStream(self, sampleNo, outputPath):
        ParametersStr = ".K_" + str(self.K) + ".iterNum_" + str(self.iterNum) + \
                        ".SampleNum_" + str(self.sampleNum) + ".alpha_" + str(round(self.alpha, 3)) + \
                        ".beta_" + str(round(self.beta, 3)) + ".BatchNum_" + str(self.AllBatchNum) + ".BatchSaved_" + str(self.MaxBatch)
        model = Model(self.K, self.MaxBatch, self.V, self.iterNum, self.alpha, self.beta, self.dataset,
                      ParametersStr, sampleNo, self.wordsInTopicNum, self.dataDir + self.timefil)
        model.run_MStream(self.documentSet, outputPath, self.wordList, self.AllBatchNum)

    def runMStreamF(self, sampleNo, outputPath):
        ParametersStr = ".K_" + str(self.K) + ".iterNum_" + str(self.iterNum) + \
                        ".SampleNum_" + str(self.sampleNum) + ".alpha_" + str(round(self.alpha, 3)) + \
                        ".beta_" + str(round(self.beta, 3)) + ".BatchNum_" + str(self.AllBatchNum) + ".BatchSaved_" + str(self.MaxBatch)
        model = Model(self.K, self.MaxBatch, self.V, self.iterNum, self.alpha, self.beta, self.dataset,
                      ParametersStr, sampleNo, self.wordsInTopicNum, self.dataDir + self.timefil)
        model.run_MStreamF(self.documentSet, outputPath, self.wordList, self.AllBatchNum)

