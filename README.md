# WORDLE
wordle in jp / en with entropy based suggestion

<img width="682" alt="スクリーンショット 2022-02-17 16 46 06" src="https://user-images.githubusercontent.com/87483306/154429124-16f0de14-9762-4deb-8c8d-e759b87396b2.png">

# Requirement
* Python3.x
* vocabulary file namely src/en/words.txt or src/jp/words.txt.
  * vocabulary file must line-separated. See _words.txt for reference.
  * English<https://github.com/dwyl/english-words>
  * Japanese<http://www17408ui.sakura.ne.jp/tatsum/english/databaseE.html>

# Usage
put line-seoarated vocabulary file on /en or /jp, named "words.txt"<br>
then, execute main.py.<br>
`python main.py`<br>
also reffer to help<br>
`python main.py -h`<br>
Note: Script will pre-compute some datas on first run. It may take few seconds, or minutes depending on how many words in vocabulary file.
