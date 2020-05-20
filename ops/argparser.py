#
# Copyright (C) 2018 Xiao Wang
# Email:xiaowang20140001@gmail.com
#

import parser
import argparse

def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-F',type=str, required=True,help='map path')#File path for our MAINMAST code
    parser.add_argument('--mode',type=int,required=True,help='0: calculating iRMSD and then prepare input randomly')
    parser.add_argument('--type',type=int,help='0:simulated map 1:real map')
    parser.add_argument('--choose',type=str,default='0',help='gpu id choose for training')
    parser.add_argument('--lr', type=float, default='0.0001', help='learning rate for training')
    parser.add_argument('--reg', type=float, default='1e-5', help='REG for training')
    parser.add_argument('--class', type=int, default='4', help='number of classes')
    parser.add_argument('--cardinality',default=32, type=int,help='ResNeXt cardinality')
    parser.add_argument('--batch_size', type=int, default='128', help='batch size for training')
    parser.add_argument('--model', type=int, default=0, help='model type for training: 0:resnet20 1:resnet50 2:resnet101 3:resnet152')
    parser.add_argument('-M', type=str,  help='model path to resume the unexpectedly stopped training')  # File path for our MAINMAST code
    parser.add_argument('--resume',type=int,default=0,help='Resume or not')
    parser.add_argument('--contour', type=float, default=0.0, help='Contour level for real map')
    parser.add_argument('--portion', type=float, default=0.8, help='validation set portion of the whole training set')
    parser.add_argument('--epochs',type=int,default=100,help='training total epochs')
    parser.add_argument('-P',type=str,default="",help="specify the list path for filtering the test data")
    parser.add_argument('--rand_seed',type=int,default=888,help="random seed in all settings")
    parser.add_argument('--use_adam',type=int,default=0,help="use adam optimizer or not, default:0")
    parser.add_argument('--drop_rate',type=float,default=0.3,help="Drop out rate for the phase2 model")
    parser.add_argument('--phase2_portion', type=float, default=0.5, help="Phase 2 portion of the training and validation")
    parser.add_argument('-M1',type=str,help="The saving path of a model used to predict it's background or not")
    parser.add_argument('-M2', type=str, help="The phase2 model saving path for evaluating")
    parser.add_argument('-M3', type=str, help="input file path for evaluation")
    parser.add_argument('--fold',type=int,default=1,help='specify the fold used for testing the real map')
    parser.add_argument('--Trimmap',type=str,default="",help="For real map, give trimmap path to help visualize simply in a fast mode")
    parser.add_argument('--Phase2_Channel',type=int,default=5,help="Specify the input channel for phase 2")
    parser.add_argument('--train_class',type=int,default=0,help="Training separate binary-model with class")
    parser.add_argument('--neighbor',type=int,default=3,help="Neighbor info used for prediction!")
    #parser.add_argument('-S',type=str,help='final training data path,preparing finish')
    #parser.add_argument('--fold', type=int, default=0, help='Resumed for training process, when is larger than 4, we use [value-4] fold as training ')
    #Dense points part parameters
    args = parser.parse_args()
    # try:
    #     import ray,socket
    #     rayinit()
    # except:
    #     print('ray need to be installed')#We do not need this since GAN can't be paralleled.
    params = vars(args)
    return params