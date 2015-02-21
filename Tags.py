import xml.sax

def onlyascii(char):
    if ord(char) == 32:
        return ' '
    elif ord(char) < 48 or ord(char) > 127: return ''
    else: return char

class MovieHandler( xml.sax.ContentHandler ):
    def __init__(self):
        self.CurrentData = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "row":
            try:
                ID = attributes['Id']
            except KeyError:
                ID = 0
            try:
                TagName = attributes['TagName']
            except KeyError:
                TagName = ""
            try:
                Count = attributes['Count']
            except KeyError:
                Count = 0
            try:
                ExcerptPostId = attributes['ExcerptPostId']
            except KeyError:
                ExcerptPostId = 0
            try:
                WikiPostId = attributes['WikiPostId']
            except KeyError:
                WikiPostId = 0
            
            data = str(ID)+","+str(TagName)+","+str(Count)+","+str(ExcerptPostId)+","+str(WikiPostId)
            print ID
            file.write(data+"\n")

if ( __name__ == "__main__"):
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    Handler = MovieHandler()
    parser.setContentHandler( Handler )

    file = open("Tags.txt","w");

    parser.parse("../../Tags.xml")
