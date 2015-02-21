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
                CreationDate = attributes['CreationDate']
            except KeyError:
                CreationDate = '2008-07-31T00:00:00.000'
            try:
                PostId = attributes['PostId']
            except KeyError:
                PostId = 0
            try:
                RelatedPostId = attributes['RelatedPostId']
            except KeyError:
                RelatedPostId = 0
            try:
                LinkTypeId = attributes['LinkTypeId']
            except KeyError:
                LinkTypeId = 0
            
            data = str(ID)+","+str(CreationDate)+","+str(PostId)+","+str(RelatedPostId)+","+str(LinkTypeId)
            print ID
            file.write(data+"\n")

if ( __name__ == "__main__"):
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    Handler = MovieHandler()
    parser.setContentHandler( Handler )

    file = open("PostLinks.txt","w");

    parser.parse("../../PostLinks.xml")
