class Solution:
  def findDuplicate(self, paths: List[str]) -> List[List[str]]:
    contentToPathFiles = collections.defaultdict(list)

    for path in paths:
      words = path.split(' ')
      rootPath = words[0]  
      for fileAndContent in words[1:]: 
        l = fileAndContent.find('(')
        r = fileAndContent.find(')')
        file = fileAndContent[:l]
        content = fileAndContent[l + 1:r]
        filePath = rootPath + '/' + file
        contentToPathFiles[content].append(filePath)

    return [filePath for filePath in contentToPathFiles.values() if len(filePath) > 1]
