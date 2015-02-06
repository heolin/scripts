#!/usr/bin/env bash
#run: ./facebook.sh messages.htm "Name Surname"
egrep '<div class="message"><div class="message_header"><span class="user">[^<]*</span><span class="meta">[^<]*</span></div></div><p>[^<]*</p>' $1 -o > _temp_messages.raw
grep "$2" _temp_messages.raw > _temp_messages.mine
egrep '<p>[^<]*</p>' _temp_messages.mine -o | sed "s/<p>//g" | sed "s/<\/p>//g" | awk '{print tolower($0)}' > _temp_result.txt
cat _temp_result.txt | ./ngram.py -n 1 -t | ./freq_list.sh > frequency.1gram
cat _temp_result.txt | ./ngram.py -n 2 -t | ./freq_list.sh > frequency.2gram
cat _temp_result.txt | ./ngram.py -n 3 -t | ./freq_list.sh > frequency.3gram
rm -rf _temp_*
