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
                PostTypeId = attributes['PostTypeId']
            except KeyError:
                PostTypeId = 0
            try:
                AcceptedAnswerId = attributes['AcceptedAnswerId']
            except KeyError:
                AcceptedAnswerId = 0
            try:
                CreationDate = attributes['CreationDate']
            except KeyError:
                CreationDate = '2008-07-31T00:00:00.000'
            try:
                Score = attributes['Score']
            except KeyError:
                Score = 0
            try:
                ViewCount = attributes['ViewCount']
            except KeyError:
                ViewCount = 0
            try:
                Body = attributes['Body']
                Body = Body.encode('ascii',errors='ignore')
                Body = ''.join(e for e in Body if onlyascii(e))
            except KeyError:
                Body = ""
            try:
                OwnerUserId = attributes['OwnerUserId']
            except KeyError:
                OwnerUserId = 0
            try:
                LastEditorUserId = attributes['LastEditorUserId']
            except KeyError:
                LastEditorUserId = 0
            try:
                LastEditorDisplayName = attributes['LastEditorDisplayName']
                LastEditorDisplayName = LastEditorDisplayName.encode('ascii',errors='ignore')
                LastEditorDisplayName = ''.join(e for e in LastEditorDisplayName if onlyascii(e))
            except KeyError:
                LastEditorDisplayName = ""
            try:
                LastEditDate = attributes['LastEditDate']
            except KeyError:
                LastEditDate = '2008-07-31T00:00:00.000'
            try:
                LastActivityDate = attributes['LastActivityDate']
            except KeyError:
                LastActivityDate = '2008-07-31T00:00:00.000'
            try:
                Title = attributes['Title']
                Title = Title.encode('ascii',errors='ignore')
                Title = ''.join(e for e in LastEditorDisplayName if onlyascii(e))
            except KeyError:
                Title = ""
            try:
                Tags = attributes['Tags']
                Tags = Tagencode('ascii',errors='ignore')
                Tags = ''.join(e for e in LastEditorDisplayName if onlyascii(e))
            except KeyError:
                Tags = ""
            try:
                AnswerCount = attributes['AnswerCount']
            except KeyError:
                AnswerCount = 0
            try:
                CommentCount = attributes['CommentCount']
            except KeyError:
                CommentCount = 0
            try:
                FavoriteCount = attributes['FavoriteCount']
            except KeyError:
                FavoriteCount = 0
            try:
                CommunityOwnedDate = attributes['CommunityOwnedDate']
            except KeyError:
                CommunityOwnedDate = '2008-07-31T00:00:00.000'

            data = str(ID)+","+str(PostTypeId)+","+str(AcceptedAnswerId)+","+str(CreationDate)+","+str(Score)+","+str(ViewCount)+","+str(Body)+","+str(OwnerUserId)+","+str(LastEditorUserId)+","+str(LastEditorDisplayName)+","+str(LastEditDate)+","+str(LastActivityDate)+","+str(Title)+","+str(Tags)+","+str(AnswerCount)+","+str(CommentCount)+","+str(FavoriteCount)+","+str(CommunityOwnedDate)
            print ID
            file.write(data+"\n")

if ( __name__ == "__main__"):
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    Handler = MovieHandler()
    parser.setContentHandler( Handler )

    file = open("Posts.txt","w");

    parser.parse("../../Posts.xml")
