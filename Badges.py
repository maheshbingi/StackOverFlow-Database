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
                UserId = attributes['UserId']
            except KeyError:
                UserId = 0
            
            try:
                Name = attributes['Name']
                Name = Name.encode('ascii',errors='ignore')
                Name = ''.join(e for e in Name if onlyascii(e))
            except KeyError:
                Name = ""

            try:
                Date = attributes['Date']
            except KeyError:
                Date = '2008-07-31T00:00:00.000'

            query = str(ID)+","+str(UserId)+","+str(Name)+","+str(Date)
            print ID
            file.write(query+"\n")

if ( __name__ == "__main__"):
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    Handler = MovieHandler()
    parser.setContentHandler( Handler )

    file = open("Badges.txt","w");

    parser.parse("../../Badges.xml")
