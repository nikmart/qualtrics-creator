count = 0
with open("videos.txt", "r") as videos:
    for clip in videos:
        print('[[Block: Block' + str(count) + ']]\n' +
        str(count) +
        '. <div><video class="qmedia" controls="true" height="360" preload="auto" width="640"><source src="' +
        clip +
        '" type="video/mp4" /><embed align="middle" autoplay="false" bgcolor="white" class="qmedia" controller="true" height="360" pluginspage="http://www.apple.com/quicktime/download/" src="'+
        clip +
        '" type="video/quicktime" width="640"></embed></video> \
           </div>Do you like this video?\n\nYes\nNo\nNo Response\n\n'
        )

        count += 1