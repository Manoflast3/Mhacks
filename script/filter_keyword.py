from textblob import TextBlob
import re

dataset = []
knowledge_base_pattern = []

#load the input comment
f = open("original_comment_dataset_small_input")
for i in f.readlines():
    if i not in ['\n', '\r\n']:
        dataset.append(i.strip("\n"))
f.close()

#load the knowledge base
f1 = open("knowledge_base.txt")
f1.readline()
f1.readline()
for i in f1.readlines():
    if i not in ['\n', '\r\n']:
        knowledge_base_pattern.append(i.strip("\n").split("|")[0])
f1.close()

f2 = open("keyword_list_without_filter", "w")
for comment in dataset:
	comment_blob = TextBlob(comment)
	comment_blob_dict = comment_blob.tags
	
	#store the letter and symbol in different string
	comment_tag_list_symbol_str = ""
	comment_tag_list_str = ""
	for i in range(0, len(comment_blob_dict)):
		if i < len(comment_blob_dict) - 1:
			comment_tag_list_symbol_str += (comment_blob_dict[i][1] + ",")
			comment_tag_list_str += (comment_blob_dict[i][0] + ",")

		else:
			comment_tag_list_symbol_str += comment_blob_dict[i][1]
			comment_tag_list_str += comment_blob_dict[i][0]
	
	#print len(comment_tag_list_str)

	#match the pattern
	begin_symbol_index = 0
	end_symbol_index = 0
	symbol_counter = 0
	symbol_tag = ""
	for j in range(0, len(knowledge_base_pattern)):
		#if match any pattern
		if knowledge_base_pattern[j] in comment_tag_list_symbol_str:
			symbol_tag = knowledge_base_pattern[j]
			begin_symbol_index = comment_tag_list_symbol_str.index(symbol_tag)
			end_symbol_index = begin_symbol_index + len(symbol_tag) - 1
			print comment_tag_list_symbol_str,
			print " " + symbol_tag
			print str(begin_symbol_index) + " " + str(end_symbol_index)
			#break
	
			#count how many "," are there in the string
			##if the the number of the , is the same both in symbal string and actual comment
			if symbol_tag.count(",") == comment_tag_list_symbol_str.count(","):
				print comment_tag_list_str.replace(",", " ")
			else:
				dot_counter1 = comment_tag_list_symbol_str[0:begin_symbol_index].count(",")
				for kk in range(0, len(comment_tag_list_str)):
					if dot_counter1 > 0:
						if comment_tag_list_str[kk] == ",":
							dot_counter1 -= 1
					else:
						break
				counter1 = kk
				print counter1

				dot_counter2 = symbol_tag.count(",") + 1
				for kkk in range(kk + 1, len(comment_tag_list_str)):
					if dot_counter2 > 0:
						if comment_tag_list_str[kkk] == ",":
							dot_counter2 -= 1
					else:
						break
				counter2 = kkk
				print counter2
				
				print comment_tag_list_str.replace(","," ")[counter1:counter2]
			break
		else:
			continue
	print "\n"
f2.close()




