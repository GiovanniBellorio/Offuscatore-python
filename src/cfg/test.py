digraph "clustertest.py" {
	graph [label="test.py"]
	1 [label="if True:
"]
	2 [label="pippo = 'pippo'
print(pippo[2])
ciao = pippo[2] + pippo[3]
print(ciao)
tmp = pippo.replace('p', 'a')
print(tmp)
ciao = pippo
prova = [pippo, pippo]
print(prova)
provs = ['a', 'b']
print(provs)
dicto = {'ciao': 'ciao'}
print(dicto)
dicto = {pippo: pippo}
print(dicto)
ciao = 'mamma'
if ciao == 'mammaa':
"]
	"2_calls" [label="print
print
pippo.replace
print
print
print
print
print
" shape=box]
	2 -> "2_calls" [label=calls style=dashed]
	4 [label="print('caso 1')
"]
	"4_calls" [label=print
 shape=box]
	4 -> "4_calls" [label=calls style=dashed]
	5 [label="print(ciao)
mamma = 'mamma'
mamma = mamma[0] + mamma[1]
print(mamma)
name = 'Kevin'
somma = 0
print('ciao')
"]
	"5_calls" [label="print
print
print
" shape=box]
	5 -> "5_calls" [label=calls style=dashed]
	7 [label="for i in range(0, 10):
"]
	8 [label="mamma = 'mamma'
somma += i
"]
	8 -> 7 [label=""]
	7 -> 8 [label="range(0, 10)
"]
	9 [label="i = 10
if i < 20:
"]
	10 [label="c = 3
"]
	11 [label="print(name, somma)
"]
	"11_calls" [label=print
 shape=box]
	11 -> "11_calls" [label=calls style=dashed]
	3 [label="cc = True
i = 0
"]
	12 [label="while i < 10:
"]
	13 [label="while False:
"]
	15 [label="print('ciao')
"]
	"15_calls" [label=print
 shape=box]
	15 -> "15_calls" [label=calls style=dashed]
	15 -> 13 [label=""]
	13 -> 15 [label=False
]
	16 [label="mamma = 'mamma'
somma += i
i += 1
"]
	16 -> 12 [label=""]
	13 -> 16 [label="(not False)
"]
	12 -> 13 [label="i < 10
"]
	14 [label="print(name, somma)
print(65 % 7)
"]
	"14_calls" [label="print
print
" shape=box]
	14 -> "14_calls" [label=calls style=dashed]
	12 -> 14 [label="(i >= 10)
"]
	3 -> 12 [label=""]
	11 -> 3 [label=""]
	10 -> 11 [label=""]
	9 -> 10 [label="i < 20
"]
	9 -> 11 [label="(i >= 20)
"]
	7 -> 9 [label=""]
	5 -> 7 [label=""]
	4 -> 5 [label=""]
	2 -> 4 [label="ciao == 'mammaa'
"]
	6 [label="ciao = 10
"]
	6 -> 5 [label=""]
	2 -> 6 [label="(ciao != 'mammaa')
"]
	1 -> 2 [label=True
]
	1 -> 3 [label="(not True)
"]
}
