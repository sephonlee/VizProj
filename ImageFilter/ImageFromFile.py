import os
from os.path import *
import tarfile
import types
import shutil

LEGAL_IMAGE_TYPE =  ('jpg', 'gif', 'tif', 'bmp', 'png', 'tiff')

class ImageFromFile:
    
        
    def __int__(self, path):
        self.path = path    
        
    def __str__(self):
        return self
    
    def setPath(self, path):
        self.path = path
        
    def getPath(self):
        return self.path

    @staticmethod
    # return all file paths from the given directory with given file Type
    # path: directory path
    # type: file type, ex: pdf, tar.gz
    def getFileNamesFromPath(path, fileType):
        print "Get file names from ", path
        fileList = []
        fileType = "." + fileType
        for dirPath, dirNames, fileNames in os.walk(path):    
            for f in fileNames:
                if f.endswith(".tar.gz"):
                    fileList.append(os.path.join(dirPath, f))
        
#         self.fileList = fileList
        return fileList
        
    @staticmethod
    # extract image file from tar file
    def extractTarFromFileName(fileName, extractTarPath, sizeThreshold = 0, legalImageType = ('jpg', 'gif', 'tif', 'bmp', 'png', 'tiff')):
#         print sizeThreshold
        if isinstance(fileName, types.StringTypes):
            # Extract files from *.tar.gz
            tfile = tarfile.open(fileName)
            if tarfile.is_tarfile(fileName):
                numExt = 0;
                numAll = 0;
                print "Extracting " + fileName + " ...." 
                for tarinfo in tfile:
#                     print tarinfo.name
#                     print tarinfo.size
                    if tarinfo.size > sizeThreshold:
                        name = tarinfo.name.split('.')
                        surfix = name[len(name) - 1]
                        if surfix in legalImageType :
                            tfile.extract(tarinfo.name, extractTarPath)
                            numExt += 1
                    numAll += 1
                print numExt , "/" , numAll , " files were extracted from " , fileName 
            else:
                print fileName + " is not a tarfile."
            tfile.close()
        else:
            print "Input fileName is illegal"

    @staticmethod
    # extract image file from tar file list
    def extractTarFromFileList(fileList, extractTarPath, sizeThreshold = 0, legalImageType = ('jpg', 'gif', 'tif', 'bmp', 'png', 'tiff')):
        if isinstance(fileList, types.ListType):
            # Extract files from *.tar.gz           
            for f in fileList:
                ImageFromFile.extractTarFromFileName(f, extractTarPath, sizeThreshold)
            print "All files were extracted in " + extractTarPath 
        else:
            print "Input fileList is illegal"

    @staticmethod
    def gatherAllFile(src, dst):
        print "Moving files from " + src
        i = 1;
        for dirPath, dirNames, fileNames in os.walk(src):
            for f in fileNames:
                fileName = f.split('.')
                fileName = 'image_%d.' % i + fileName[len(fileName)-1];
                newDst = dst + fileName
                shutil.move(os.path.join(dirPath, f), newDst)
                i += 1
        print "All files were moved to " + dst
        # delete rest files and folders
        for dirPath, dirNames, fileNames in os.walk(src):
            for name in fileNames:
                os.remove(os.path.join(dirPath, name))
            for name in dirNames:
                print os.path.join(dirPath, name)
                os.rmdir(os.path.join(dirPath, name))
        os.rmdir(src)
        print "Removed " + src

if __name__ == '__main__':   
    
    path = "/Users/sephon/Documents/workspace/VizPDF/papers/Pubmed/ee/"
    f = '/Users/sephon/Documents/workspace/VizPDF/papers/Pubmed/f8/BMC_Cell_Biol_2011_Jul_25_12_31.tar.gz'
    extractTarPath = '/Users/sephon/Documents/workspace/VizPDF/papers/Pubmed/extImages/'
        
    
    fileList = ImageFromFile.getFileNamesFromPath(path, "tar.gz")
    
    # 
#     ImageFromFile.extractTarFromFileName(f, extractTarPath, 8000)


#     ImageFromFile.extractTarFromFileList(fileList, extractTarPath, 8000)

    
    dst = "/Users/sephon/Documents/workspace/VizPDF/papers/Pubmed/allImages/"
    ImageFromFile.gatherAllFile(extractTarPath, dst)


        