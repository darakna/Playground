from mutagen.mp3 import MP3
import os

f = open("all_mp3s.txt", "rb")
bulk_file = f.read()
g = open("toata_muzica.txt", "wb")
for a in bulk_file.split("\n".encode()):
    try:
        if os.path.exists(a):
            amp3 = MP3(a)
            if amp3.info.length / 60 > 2:
                time_min_sec = "{:02d}:{:02d}".format(int(amp3.info.length / 60), int(amp3.info.length % 60))
                size_kb = "{:6.3f} mb".format(os.path.getsize(a) / 1024 / 1024)
                line = time_min_sec.encode() + " :: ".encode() + size_kb.encode() + " :: ".encode() + a + "\n".encode()
                g.write(line)
    except:
        line = "err :: err :: ".encode() + a + "\n".encode()
        g.write(line)
        print("MP3 Header Error on file: ", a)


f.close()
g.close()
