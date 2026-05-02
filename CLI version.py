# -*- coding: utf-8 -*-
"""
Chem3D-Viewer
Developed by Ali Chaudhary (Greenshaw)
Simple formula visualiser using RDKit and py3dMol
License: MIT
"""


#ali
#put the formula in a 'SMILE' form
#Single bonds are assumed like 'CO'
# use = for double bonds or # for triple bonds


from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

#standard imports

def model_3d(smiles):
  mol = Chem.MolFromSmiles(smiles)
  #creates the molecule
  mol = Chem.AddHs(mol)
  #adds hydrogen because for some reason its normally ignored

  AllChem.EmbedMolecule(mol, AllChem.ETKDG())
  #calculates 3d positions based on lengths
  #takes the molecule text and makes it into a mol object python can read
  AllChem.MMFFOptimizeMolecule(mol)
  #optimises by finding a stable version of the molecule


  mblock = Chem.MolToMolBlock(mol)
  view = py3Dmol.view(width=400, height=400)
  view.addModel(mblock, 'mol')
  #makes a 3d viewer

  view.setStyle({'stick': {}, 'sphere': {'scale': 0.3}})
  view.zoomTo()
  return view.show()
  #closest thing to the simple ball and stick model


#this is a basic menu and the only user interface
def menu():
  print("molecule viewing simulator")
  print("")
  print("")
  print("remember how to format the SMILE mol")
  print("single bonds are assumed, double are = and triple are #")
  print("examples are CO or O=C=O")
  print("")
  print("")
  print("press 1 to start or 0 to exit")
  flaginput=False
  while flaginput==False:
    try:
      user=int(input("enter: "))
      if user==1 or user==0:
        flaginput=True
      else:
        flaginput=False
    except:
      print("invalid user")
  if user==1:
    try:
      model_3d(input("mol string: "))
      menu()
    except:
      print("invalid mol string format ")

  elif user==0:
    exit()

menu()

