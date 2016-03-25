# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 13:29:28 2016

@author: nfett
"""

import sys
from blocktools import *
from block import Block, BlockHeader

def parse(blockchain):
    counter = 0
    while True:
        block= Block(blockchain, counter)
        block.toString(counter)
        counter+=1
def main():
    if len(sys.argv) < 2:
        print 'Usage: blockparser.py filename'
    else:
        print "Block_Number,Magic_Number,Blocksize,Version,Prev_blockHash,Merkle_Root,Time,Difficulty,Nonce,Tx_Count,trade_id,Tx_Version,Inputs,Prev_Hash,Tx_Out_Index,Script_Length,Script_Sig,Sequence,Output,Value,Script_Len,Pubkey,Locktime"
        with open(sys.argv[1], 'rb' ) as blockchain:
            parse(blockchain)
            
if __name__ == '__main__':
    main()