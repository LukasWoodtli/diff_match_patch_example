import diff_match_patch as dmp_module

dmp = dmp_module.diff_match_patch()

s1 = ""
s2 = ""

with open("diff_text_1.txt", 'r') as f:
    s1 = f.read()

with open("diff_text_2.txt", 'r') as f:
    s2 = f.read()

diff_result = dmp.diff_main(s1, s2)
#with open('diff.htm', 'w') as f:
#    f.write(dmp.diff_prettyHtml(diff_result))

#dmp.diff_cleanupSemantic(diff_result)
dmp.diff_cleanupEfficiency(diff_result)

print diff_result

for i in xrange(len(diff_result)):
    for j in xrange(i+1, len(diff_result)):
        if diff_result[j][1] == diff_result[i][1]: # and diff_result[i][0] * diff_result[j][0] == -1:
           pass # print diff_result[i], diff_result[j]
