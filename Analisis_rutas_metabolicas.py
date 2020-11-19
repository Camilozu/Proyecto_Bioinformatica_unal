# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:12:49 2020

@author: camil
"""
import os
import sys
try:
    archivo_a_ensamblar = sys.argv[1]
    archivo_a_ensamblar_pareado = sys.argv[2]
    print("x2")
    os.system("seqtk trimfq "+archivo_a_ensamblar+" > "+"archivo_a_ensamblar_trim.fq")
    os.system("seqtk trimfq "+archivo_a_ensamblar_pareado+" > "+"archivo_a_ensamblar_pareado_trim.fq")
    os.system("spades.py -o ensamblaje_de_novo --rna --pe1-1 archivo_a_ensamblar_trim.fq --pe1-2 archivo_a_ensamblar_pareado_trim.fq")
except:
    archivo_a_ensamblar = sys.argv[1]
    os.system("seqtk trimfq "+archivo_a_ensamblar+" > "+"archivo_a_ensamblar_trim.fq")
    print("x1")
    os.system("spades.py -o ensamblaje_de_novo --rna --pe1-1 archivo_a_ensamblar_trim.fq")

Transcriptoma = os.system("ensamblaje_de_novo/transcripts.fasta")
