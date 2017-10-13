# -*- coding: utf-8 -*-
import operator, os, sys
import numpy as np
import time

#En el siguiente método se obtienen los archivos y se recorren para obtener las palabras más importantes de cada uno
def obtTFiles(rootDir):
    T = []
    for nombreDir, subdirList, fileList in os.walk(rootDir):
        print('Directorio encontrado: %s' % nombreDir)
        for archivo in fileList:

            archivo = open(rootDir + archivo, 'r')

            #Éstas son las palabras que se deben eliminar de cada archivo que se lee

            stopwords = ["a", "able", "about", "above", "according", "accordingly", "across", "actually", "after",
                         "afterwards", "again", "against", "all", "allow", "allows", "almost", "alone", "along",
                         "already", "also", "although", "always", "am", "among", "amongst", "an", "and", "another",
                         "any", "anybody", "anyhow", "anyone", "anything", "anyway", "anyways", "anywhere", "apart",
                         "appear", "appreciate", "appropriate", "are", "around", "as", "aside", "ask", "asking",
                         "associated", "at", "available", "away", "awfully", "b", "be", "became", "because", "become",
                         "becomes", "becoming", "been", "before", "beforehand", "behind", "being", "believe", "below",
                         "beside", "besides", "best", "better", "between", "beyond", "both", "brief", "but", "by", "c",
                         "came", "can", "cannot", "cant", "cause", "causes", "certain", "certainly", "changes",
                         "clearly", "co", "com", "come", "comes", "concerning", "consequently", "consider",
                         "considering", "contain", "containing", "contains", "corresponding", "could", "course",
                         "currently", "d", "definitely", "described", "despite", "did", "different", "do", "does",
                         "doing", "done", "down", "downwards", "during", "e", "each", "edu", "eg", "eight", "either",
                         "else", "elsewhere", "enough", "entirely", "especially", "et", "etc", "even", "ever", "every",
                         "everybody", "everyone", "everything", "everywhere", "ex", "exactly", "example", "except", "f",
                         "far", "few", "fifth", "first", "five", "followed", "following", "follows", "for", "former",
                         "formerly", "forth", "four", "from", "further", "furthermore", "g", "get", "gets", "getting",
                         "given", "gives", "go", "goes", "going", "gone", "got", "gotten", "greetings", "h", "had",
                         "happens", "hardly", "has", "have", "having", "he", "hello", "help", "hence", "her", "here",
                         "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "hi", "him", "himself", "his",
                         "hither", "hopefully", "how", "howbeit", "however", "i", "ie", "if", "ignored", "immediate",
                         "in", "inasmuch", "inc", "indeed", "indicate", "indicated", "indicates", "inner", "insofar",
                         "instead", "into", "inward", "is", "it", "its", "itself", "j", "just", "k", "keep", "keeps",
                         "kept", "know", "knows", "known", "l", "last", "lately", "later", "latter", "latterly",
                         "least", "less", "lest", "let", "like", "liked", "likely", "little", "ll", "look", "looking",
                         "looks", "ltd", "m", "mainly", "many", "may", "maybe", "me", "mean", "meanwhile", "merely",
                         "might", "more", "moreover", "most", "mostly", "much", "must", "my", "myself", "n", "name",
                         "namely", "nd", "near", "nearly", "necessary", "need", "needs", "neither", "never",
                         "nevertheless", "new", "next", "nine", "no", "nobody", "non", "none", "noone", "nor",
                         "normally", "not", "nothing", "novel", "now", "nowhere", "o", "obviously", "of", "off",
                         "often", "oh", "ok", "okay", "old", "on", "once", "one", "ones", "only", "onto", "or", "other",
                         "others", "otherwise", "ought", "our", "ours", "ourselves", "out", "outside", "over",
                         "overall", "own", "p", "particular", "particularly", "per", "perhaps", "placed", "please",
                         "plus", "possible", "presumably", "probably", "provides", "q", "que", "quite", "qv", "r",
                         "rather", "rd", "re", "really", "reasonably", "regarding", "regardless", "regards",
                         "relatively", "respectively", "right", "s", "said", "same", "saw", "say", "saying", "says",
                         "second", "secondly", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self",
                         "selves", "sensible", "sent", "serious", "seriously", "seven", "several", "shall", "she",
                         "should", "since", "six", "so", "some", "somebody", "somehow", "someone", "something",
                         "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "specified", "specify",
                         "specifying", "still", "sub", "such", "sup", "sure", "t", "take", "taken", "tell", "tends",
                         "th", "than", "thank", "thanks", "thanx", "that", "thats", "the", "their", "theirs", "them",
                         "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein",
                         "theres", "thereupon", "these", "they", "think", "third", "this", "thorough", "thoroughly",
                         "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too",
                         "took", "toward", "towards", "tried", "tries", "truly", "try", "trying", "twice", "two", "u",
                         "un", "under", "unfortunately", "unless", "unlikely", "until", "unto", "up", "upon", "us",
                         "use", "used", "useful", "uses", "using", "usually", "uucp", "v", "value", "various", "ve",
                         "very", "via", "viz", "vs", "w", "want", "wants", "was", "way", "we", "welcome", "well",
                         "went", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter",
                         "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while",
                         "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "willing", "wish",
                         "with", "within", "without", "wonder", "would", "would", "x", "y", "yes", "yet", "you", "your",
                         "yours", "yourself", "yourselves", "z", "zero"]
            principalwords = {}

            #En esta parte se lee cada archivo y se verifican las palabras que no hacen parte de las stopwords
            #Además se añaden a una lista las palabras más repetidas de cada archivo.
            for linea in archivo:

                for palabra in linea.split():
                    palabra = palabra.strip().lower().replace(",", "").replace(":", "").replace(";", "").replace("-","").replace(".",
                    "").replace("\"", "").replace("]", "").replace("[", "").replace(")", "").replace("(", "")
                    if palabra not in stopwords:
                        if palabra in principalwords and palabra != '':
                            principalwords[palabra] += 1
                        else:
                            principalwords[palabra] = 1

            sorted_mainwords = sorted(principalwords.items(), key=operator.itemgetter(1))[::-1]

            finalwords = {}
            for i in range(10):
                finalwords[sorted_mainwords[i][0]] = sorted_mainwords[i][1]

            T.extend([element for element in list(finalwords.keys()) if element not in T])

    return T


#Éste método sirve para obtener un diccionario de cada archivo y sus 10 palabras más importantes
def ft(T):
    mapa = {}

    for nombreDir, subdirList, fileList in os.walk(rootDir):
        for archivo in fileList:
            result = []
            for i in range(len(T)):
                result.append(0)

            archivo = open(rootDir + archivo, 'r')

            for linea in archivo:
                for palabra in linea.split():
                    palabra = palabra.strip().lower().replace(",", "").replace(":", "").replace(";", "").replace("-","").replace(".",
                     "").replace("\"", "").replace("]", "").replace("[", "").replace(")", "").replace("(", "")
                    if palabra in T:
                        result[T.index(palabra)] += 1

            mapa[archivo] = result

    return mapa


#Con éste método creamos una matriz que tiene las distancias de todos los archivos que se están comparando.
def jaccard(fdt):
    tam = len(fdt)
    matrizI = np.empty((tam, tam))

    listaArchi = list(fdt.keys())

    for i in range(tam):
        for j in range(tam):
            matrizI[i][j] = 1.0 - (jaccard_similarity(fdt[listaArchi[i]], fdt[listaArchi[j]]))

    return matrizI


#Éste método es el que realiza la función (Intersección/Unión) que nos sirve para obtener las distancias entre dos archivos
def jaccard_similarity(x, y):
    intersectionC = len(set.intersection(*[set(x), set(y)]))
    # print(intersectionC)
    unionC = len(set.union(*[set(x), set(y)]))
    # print(list(set.union(*[set(x), set(y)])))
    return intersectionC / float(unionC)

#Éste es el método que sirve para saber que centro tiene cada grupo de archivos y para recalcular ese centro
def kMeans(X, K, maxIters=10, plot_progress=None):
    centroidesI = X[np.random.choice(np.arange(len(X)), K), :]
    for i in range(maxIters):
        # Cluster Assignment step
        C = np.array([np.argmin([np.dot(x_i - y_k, x_i - y_k) for y_k in centroidesI]) for x_i in X])
        #print(np.array([np.argmin([np.dot(x_i - y_k, x_i - y_k) for y_k in centroidesI]) for x_i in X]))
        # Move centroidesI step
        centroidesI = [X[C == k].mean(axis=0) for k in range(K)]
        if plot_progress != None: plot_progress(X, C, np.array(centroidesI))
    return np.array(centroidesI), C

def kMeans2(X, K, maxIters=10, plot_progress=None):
    centroidesI = X[np.random.choice(np.arange(len(X)), K), :]
    C = []
    for i in range(maxIters):
        argminList = []
        for x_i in X:
            dotList = []
            for y_k in centroidesI:
                dotList.append(np.dot(x_i - y_k, x_i - y_k))
            argminList.append(np.argmin(dotList))
        C = np.array(argminList)
        centroidesTemp = []
        for k in range(K):
            tfArr = C == k
            propiosKArr = X[tfArr]
            promedioArr = propiosKArr.mean(axis=0)
            centroidesTemp.append(promedioArr)
        centroidesI = centroidesTemp
    return np.array(centroidesI), C

if __name__ == '__main__':
    timeini = time.time()
    k = 2
    rootDir = sys.argv[1]
    T = obtTFiles(rootDir)
    fdt = ft(T)
    print(time.time()-timeini)

    matrizJaccard = jaccard(fdt)

    centroides, finalList = kMeans2(matrizJaccard, k)
    print("Tiempo final: ", time.time() - timeini)

    listaArchi = list(fdt.keys())
    cluster0 = []
    cluster1 = []
    for i in range(len(listaArchi)):
        if finalList[i] == 0:
            cluster0.append(listaArchi[i])
        else:
            cluster1.append(listaArchi[i])

    print("Cluster 0: ", cluster0)
    print("Cluster 1: ", cluster1)