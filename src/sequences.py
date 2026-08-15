

!pip install biopython
import Bio

#----------------------------------------------
#   CONTEO DE NUCLEÓTIDOS
#-----------------------------------------------

import os

def contar_nucleotidos(fasta="multipleSeqs.fa", organismo=''):
  with open ("multipleSeqs.fa", 'r') as fasta:  # leemos el archivo fasta
    lineas = [linea.rstrip(os.linesep) for linea in fasta.readlines()]  # creamos una lista en la que cada elemento es una línea del archivo fasta

  # creamos un diccionario donde las claves son los identificadores que comienzan por '>'
  # y los valores serán las secuencias
  seqs = {}
  for linea in range(len(lineas)):
    if lineas[linea].startswith('>'):
      for line in range(linea+1, len(lineas)):
        if lineas[line].startswith('>'):
          break
        else:
          if lineas[linea] in seqs:
            seqs[lineas[linea]] = seqs[lineas[linea]] + lineas[line]
          else:
            seqs[lineas[linea]] = lineas[line]

    # a continuación, iteramos sobre las claves del diccionario, si contienen el
    # organimos dado, se añadirá a un nuevo diccionario junto con los contajes de los
    # diferentes nucleótidos
  nucleotidos = {}
  for identificador in seqs:
    if organismo.lower() in identificador.lower():
       nucleotidos[identificador[1:12]] = {"A": seqs[identificador].count("A"),  # añadimos el [1:12] para que la clave sea solo el identificador, sin '>'
                                    "C": seqs[identificador].count("C"),
                                    "G": seqs[identificador].count("G"),
                                    "T": seqs[identificador].count("T")}

  return nucleotidos

# -------------------------------------
#   PIECHARTS DE COMPOSICIÓN DE BASES
# -------------------------------------

from Bio import SeqIO
import matplotlib.pyplot as plt

def pie_chart_bases(fasta_file):
  records = SeqIO.parse(fasta_file, "fasta")  # leemos el archivo fasta
  counts = {}                                 # creamos un diccionario vacío donde guardaremos la cuantas bases hay de cada
  for seq_record in records:                  # para cada secuencia contamos las 4 bases y las guardamos en el diccionario
    counts["A"] = seq_record.seq.count("A")
    counts["T"] = seq_record.seq.count("T")
    counts["C"] = seq_record.seq.count("C")
    counts["G"] = seq_record.seq.count("G")
    plt.pie(counts.values(), autopct = '%1.1f%%', labels = list(counts.keys()) )    # representamos los valores del diccionario, con su porcentaje (autopct) y ponemos como etiquetas las claves
    plt.title("Composición de Bases en Secuencia " +  seq_record.id)      # añadimos el título con el id de la secuencia
    plt.show()                                                             # e indicamos que se muestre el gráfico de cada iteración, que se corresponderá a cada secuencia

# --------------------------------------------
#   REVERSA COMPLEMENTARIA
# --------------------------------------------

from Bio.Seq import Seq
def complementaria(sec):
  seq = Seq(sec)                          # pasamos la secuencia a un objeto Seq de bipython
  rev_comp = seq.reverse_complement()     # así podemos utilizar la función reverse_complement()
  return rev_comp                         # que nos dará la reversa complementaria de la secuencia

# --------------------------------------------
#   DISTANCIA DE HAMMING
# --------------------------------------------

def hamming(p, q):
  dist = 0                      # creamos un contador para la distancia
  for i in range(len(p)):       # por cada posición en p y q
    if p[i] != q[i]:            # si la base es distinta
      dist += 1                 # sumamos 1 a la distancia
  return dist

# --------------------------------------------
#   MUTACIONES PUNTUALES
# --------------------------------------------

def rel_trans(s1, s2):
  transiciones = 0
  transversiones = 0
  for i in range(len(s1)):                      # para cada base en las secuencias
    if s1[i] != s2[i]:                          # comprobamos si son distintas
      if (s1[i] == 'A') or (s1[i] == 'G'):      # si lo son, en caso de que en la cadena 1 tengamos una A o G
        if (s2[i] == 'A') or (s2[i] == 'G'):    # si en la cadena dos también hay una A o G,
          transiciones += 1                     # añadimos una transición
        if (s2[i] == 'C') or (s2[i] == 'T'):    # si en la cadena 2 hay una C o T,
          transversiones += 1                   # añadimos una transversión
      if (s1[i] == 'T') or (s1[i] == 'C'):      # en caso de que en la cadena 1 tengamos una T o C:
        if (s2[i] == 'T') or (s2[i] == 'C'):    # si en la cadena 2 también hay una T o C
          transiciones += 1                     # Añadimos una transición
        if (s2[i] == 'A') or (s2[i] == 'G'):    # y si en la cadena 2 hay una A o G,
          transversiones += 1                   # añadimos una transversión
  r = transiciones / transversiones             # calculamos la relación entre transición y transversión
  return r
