import os
from os.path import *
import tarfile


for response in os.walk("/Users/sephon/Documents/workspace/VizPDF/papers/Pubmed"):
    print response
PATH = "/Users/sephon/Documents/workspace/VizPDF/papers/Pubmed"
IMGSIZETHRHD = 1000

# for dirPath, dirNames, fileNames in os.walk(PATH):
#     print dirPath
#     for f in fileNames:
#         print os.path.join(dirPath, f)

tarGzFileList = []
pdfFileList = [];
    
for dirPath, dirNames, fileNames in os.walk(PATH):
     
#     print sum(getsize(join(dirPath,name)) for name in fileNames)        
#     if '.DS_Store' in fileNames:
#         fileNames.remove('.DS_Store')
        
    for f in fileNames:
        fileType = ".", "tar.gz"
        if f.endswith(fileType):
            tarGzFileList.append(os.path.join(dirPath, f))
        if f.endswith(".pdf"):
            pdfFileList.append(os.path.join(dirPath, f))

f = '/Users/sephon/Documents/workspace/VizPDF/papers/Pubmed/f8/BMC_Cell_Biol_2011_Jul_25_12_31.tar.gz'
extractTarPath = '/Users/sephon/Documents/workspace/VizPDF/papers/Pubmed/extImages/'

for f in tarGzFileList:
    print "Extracting ", f, " ...." 


# Extract files from *.tar.gz
# for f in tarGzFileList:
# print "Extracting ", f, " ...." 
# tfile = tarfile.open(f)
# if tarfile.is_tarfile(f):
# 
#     # list all contents
# #         print "tar file contents:"
# #         print tfile.list(verbose=False)
#     numExt = 0;
#     numAll = 0;
#     for tarinfo in tfile:
#         if tarinfo.size > IMGSIZETHRHD:
#             tfile.extract(tarinfo.name, extractTarPath)
#             numExt += 1
#         numAll += 1
#             
#     print numExt, "/", numAll, " files were extracted from ", f  
# else:
#     print f + " is not a tarfile."
# tfile.close()





#     for f in fileNames:
#         print(a.endswith("."))
#         f.endswith("pdf")
#             fileNames.remove(f)
            
#         print(f.endswith("pdf"))
#         print f
#         dirPath.remove('')
#         os.path.join(dirPath, f).
#         print "bytes in", len(f)
#         print os.path.join(dirPath, f)
        
        