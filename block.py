# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 13:21:16 2016

@author: nfett
"""
import re

from blocktools import *

class BlockHeader: 
	def __init__(self, blockchain): 
         self.version = uint4(blockchain) 
         self.previousHash = hash32(blockchain) 
         self.merkleHash = hash32(blockchain) 
         self.time = uint4(blockchain) 
         self.bits = uint4(blockchain) 
         self.nonce = uint4(blockchain) 
        
	def toString(self,counter, magicNum, blocksize): 
         blockstring= str(counter) + "," + str(magicNum)+ "," + str(blocksize)+ "," + str(self.version)+ "," + str(hashStr(self.previousHash))+ "," + str(hashStr(self.merkleHash))+ "," + str(self.time)+ "," + str(self.bits)+ "," + str(self.nonce)
         return blockstring
 
class Block: 
	def __init__(self, blockchain, counter): 
		self.magicNum = uint4(blockchain) 
		self.blocksize = uint4(blockchain) 
		self.setHeader(blockchain) 
		self.txCount = varint(blockchain) 
		self.Txs = [] 
 
		for i in range(0, self.txCount): 
			tx = Tx(blockchain) 
			self.Txs.append(tx) 
 
	def setHeader(self, blockchain): 
		self.blockHeader = BlockHeader(blockchain) 
 
	def toString(self, counter):  
         newblock=self.blockHeader.toString(counter, self.magicNum, self.blocksize) + "," + str(self.txCount)
         trade_id=1
         for t in self.Txs: 
                 t.toString(newblock,trade_id)
                 trade_id+=1
 
class Tx: 
	def __init__(self, blockchain): 
		self.version = uint4(blockchain) 
		self.inCount = varint(blockchain) 
		self.inputs = [] 
		for i in range(0, self.inCount): 
			input = txInput(blockchain) 
			self.inputs.append(input) 
		self.outCount = varint(blockchain) 
		self.outputs = [] 
		if self.outCount > 0: 
			for i in range(0, self.outCount): 
				output = txOutput(blockchain) 
				self.outputs.append(output)	 
		self.lockTime = uint4(blockchain) 
		 
	def toString(self,newblock,trade_id):
            transaction=newblock + "," + str(trade_id)  + "," + str(self.version) + "," +str(self.inCount)
            for i in self.inputs: 
                in_exp = transaction + "," + i.toString() + "," + str(self.outCount)
                for o in self.outputs: 
                    out_exp=in_exp + "," + o.toString() + "," +str(self.lockTime)
                    print out_exp

 
class txInput: 
	def __init__(self, blockchain): 
		self.prevhash = hash32(blockchain) 
		self.txOutId = uint4(blockchain) 
		self.scriptLen = varint(blockchain) 
		self.scriptSig = blockchain.read(self.scriptLen) 
		self.seqNo = uint4(blockchain) 
 
	def toString(self):
             oneinput=str(hashStr(self.prevhash))+ "," +str(self.txOutId) + "," + str(self.scriptLen) + "," + str(hashStr(self.scriptSig)) + "," +str(self.seqNo)
             return oneinput
	 
		 
class txOutput: 
	def __init__(self, blockchain):	 
		self.value = uint8(blockchain) 
		self.scriptLen = varint(blockchain) 
		self.pubkey = blockchain.read(self.scriptLen) 
 
	def toString(self): 
             oneoutput=str(self.value) + "," + str(self.scriptLen) + "," + str(hashStr(self.pubkey))
             return oneoutput
