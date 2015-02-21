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
                Reputation = attributes['Reputation']
            except KeyError:
                Reputation = 0
            
            try:
                CreationDate = attributes['CreationDate']
            except KeyError:
                CreationDate = '2008-07-31T00:00:00.000'
            
            try:
                DisplayName = attributes['DisplayName']
                DisplayName = DisplayName.encode('ascii',errors='ignore')
                DisplayName = ''.join(e for e in DisplayName if onlyascii(e))
            except KeyError:
                DisplayName = ""

            try:
                LastAccessDate = attributes['LastAccessDate']
            except KeyError:
                LastAccessDate = '2008-07-31T00:00:00.000'            
            
            try:
                WebsiteUrl = attributes['WebsiteUrl']
                WebsiteUrl = WebsiteUrl.encode('ascii',errors='ignore')
                WebsiteUrl = ''.join(e for e in WebsiteUrl if onlyascii(e))
            except KeyError:
                WebsiteUrl = ""

            try:
                Location = attributes['Location']
                Location = Location.encode('ascii',errors='ignore')
                Location = ''.join(e for e in Location if onlyascii(e))
            except KeyError:
                Location = ""

            try:                
                AboutMe = attributes['AboutMe']
                AboutMe = AboutMe.encode('ascii',errors='ignore')
                AboutMe = ''.join(e for e in AboutMe if onlyascii(e))
            except:
                AboutMe = ""

            try:    
                Views = attributes['Views']
            except:
                Views = 0

            try:
                UpVotes = attributes['UpVotes']
            except:
                UpVotes = 0

            try:
                DownVotes = attributes['DownVotes']
            except:
                DownVotes = 0

            try:
                AccountId = attributes['AccountId']
            except:
                AccountId = 0

            query = str(ID)+","+str(Reputation)+","+str(CreationDate)+","+str(DisplayName)+","+str(LastAccessDate)+","+str(WebsiteUrl)+","+str(Location)+","+str(AboutMe)+","+str(Views)+","+str(UpVotes)+","+str(DownVotes)+","+str(AccountId)
            print ID
            file.write(query+"\n")

if ( __name__ == "__main__"):
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    Handler = MovieHandler()
    parser.setContentHandler( Handler )

    file = open("Users.txt","w");

    parser.parse("../../Users.xml")
