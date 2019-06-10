# -*- coding: utf-8 -*-
"""
Create the Farey FInite Fractal as a sampling pattern for MRI

All figures and code pertaining to the display, saving and generation of fractals, 
are covered under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 
International Public License: http://creativecommons.org/licenses/by-nc-sa/4.0/.
For publication and commercial use of this content, please obtain a suitable license 
from Shekhar S. Chandra.
"""
from __future__ import print_function    # (at top of module)
import _libpath #add custom libs
import finitetransform.numbertheory as nt #local modules
import finitetransform.mojette as mojette
import finitetransform.radon as radon
import finitetransform.imageio as imageio #local module
import finitetransform.farey as farey #local module
import numpy as np
import skimage as ski

#plot slices responsible for reconstruction
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm 

###parameters
##N = 512
##M = 2*N
##K = 1
##twoQuads = True
##print("N:", N, "M:", M)
###p = nt.nearestPrime(M)
###print("p:", p)
###pDash = nt.nearestPrime(N)
###print("p':", pDash)
###angles = mojette.angleSet_Finite(pDash, 2)
##angles, lengths = mojette.angleSet_Symmetric(N,N,1,True,K) #here
###getProjectionCoordinates
##perpAngle = farey.farey(1,0)
##angles.append(perpAngle)
##print("Number of Angles:", len(angles))
##print("angles:", angles)
##
###powerSpect = np.zeros((p,p))
##powerSpect = np.zeros((M,M))
##
###np.set_printoptions(threshold=np.nan)
##
###compute lines
##print("Computing Finite lines...")
##centered = True
##mLines = []
##sLines = []
##mValues = []
##sValues = []
##pValues = []
##qValues = []
##for angle in angles:
##    #m, inv = farey.toFinite(angle, p)
##    #u, v = radon.getSliceCoordinates2(m, powerSpect, centered, p)
##    m, s, p, q, inv = farey.toFinite(angle, M)
##    pValues.append(p)
##    qValues.append(q)
##    if m not in mValues and m < M:
##        print("m: ", m)
##        u, v = radon.getSliceCoordinates2(m, powerSpect, centered, M)
##        mLines.append((u,v))
##        mValues.append(m)
##    if s not in sValues and N+s < 0.75*M and N-s > 0:
##        print("s: ", N+s)
##        print("s: ", N-s)
##        u, v = radon.getSliceCoordinates2(N-s, powerSpect, centered, M)
##        sLines.append((u,v))
##        u, v = radon.getSliceCoordinates2(N+s, powerSpect, centered, M)
##        sLines.append((u,v))
##        u, v = radon.getSliceCoordinates2(s, powerSpect, centered, M)
##        sLines.append((u,v))
##        sValues.append(N+s)
##        sValues.append(N-s)
##        sValues.append(s)
##
##    
##    #second quadrant
##    if twoQuads:
##        #if m != 0 and m != p: #dont repeat these
##        if m != 0 and m != M: #dont repeat these
##            #m = p-m
##            #u, v = radon.getSliceCoordinates2(m, powerSpect, centered, p)
##            m = M-m
##            if m not in mValues and m < M:
##                print("m: ", m)
##                u, v = radon.getSliceCoordinates2(m, powerSpect, centered, M)
##                mLines.append((u,v))
##                mValues.append(m)
##
##            s = N/2-s
##            if s not in sValues and N+s < 0.75*M and N-s > 0:
##                print("s: ", N+s)
##                print("s: ", N-s)
##                u, v = radon.getSliceCoordinates2(N-s, powerSpect, centered, M)
##                sLines.append((u,v))
##                u, v = radon.getSliceCoordinates2(N+s, powerSpect, centered, M)
##                sLines.append((u,v))
##                u, v = radon.getSliceCoordinates2(s, powerSpect, centered, M)
##                sLines.append((u,v))
##                sValues.append(N+s)
##                sValues.append(N-s)
##                sValues.append(s)
##                
##
##
##angles1, lengths1 = mojette.angleSet_Symmetric(N,N,1,True,2) #here
##perpAngle1 = farey.farey(1,0)
##angles1.append(perpAngle1)
##
##for angle in angles1:
##    #m, inv = farey.toFinite(angle, p)
##    #u, v = radon.getSliceCoordinates2(m, powerSpect, centered, p)
##    m, s, p, q, inv = farey.toFinite(angle, M)
##    pValues.append(p)
##    qValues.append(q)
##    if s not in sValues and N+s < 0.75*M and N-s > 0:
##        print("s: ", N+s)
##        print("s: ", N-s)
##        u, v = radon.getSliceCoordinates2(N-s, powerSpect, centered, M)
##        sLines.append((u,v))
##        u, v = radon.getSliceCoordinates2(N+s, powerSpect, centered, M)
##        sLines.append((u,v))
##        u, v = radon.getSliceCoordinates2(s, powerSpect, centered, M)
##        sLines.append((u,v))
##        sValues.append(N+s)
##        sValues.append(N-s)
##        sValues.append(s)
##    #u, v = radon.getSliceCoordinates2(m, powerSpect, centered, M)
##    #mLines.append((u,v))
##    #mValues.append(m)
##
##    
##    #second quadrant
##    if twoQuads:
##        #if m != 0 and m != p: #dont repeat these
##        if m != 0 and m != M: #dont repeat these
##            #m = p-m
##            #u, v = radon.getSliceCoordinates2(m, powerSpect, centered, p)
##            m = M-m
##            #u, v = radon.getSliceCoordinates2(m, powerSpect, centered, M)
##            #mLines.append((u,v))
##            #mValues.append(m)
##        s = N/2-s            
##        if s not in sValues and N+s < 0.75*M and N-s > 0:
##            print("s: ", N+s)
##            print("s: ", N-s)
##            u, v = radon.getSliceCoordinates2(N-s, powerSpect, centered, M)
##            sLines.append((u,v))
##            u, v = radon.getSliceCoordinates2(N+s, powerSpect, centered, M)
##            sLines.append((u,v))
##            u, v = radon.getSliceCoordinates2(s, powerSpect, centered, M)
##            sLines.append((u,v))
##            sValues.append(N+s)
##            sValues.append(N-s)
##            sValues.append(s)
##
##
##mu = len(mLines)
##print("Number of lines:", len(mLines))
###print("Proportion of p:", len(lines)/float(p))
###print("Proportion of 2D space:", 2.0-len(lines)/float(p))
##print("Proportion of M:", (len(mLines)+len(sLines))/float(M))
##print("Proportion of 2D space:", 2.0-(len(mLines)+len(sLines))/float(M))
##print(mValues)
##print(sValues)
##print(pValues)
##print(qValues)
##print("Number of m lines:", len(mLines))
##print("Number of s lines:", len(sLines))
##print("Proportion of M:", (len(mLines)+len(sLines))/float(M))
##print("Proportion of 2D space:", 2.0-(len(mLines)+len(sLines))/float(M))
##
###plot slices responsible for reconstruction
##import matplotlib.pyplot as plt
##from matplotlib.pyplot import cm 
##
##fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))
##
##plt.gray()
##plt.tight_layout()
##
##maxLines = len(sLines+mLines)
##i = 0
###maxLines = 12
##ax[0].imshow(powerSpect)
##ax[1].imshow(powerSpect)
###color=iter(cm.rainbow(np.linspace(0,1,len(lines))))
##color=iter(cm.jet(np.linspace(0,1,maxLines+1)))
##fareyImage = np.zeros_like(powerSpect)
##for i, sLine in enumerate(sLines):
##    u, v = sLine
##    #c=next(color)
##    #ax[0].plot(u, v, '.', c=c, markersize=1)
##    ax[1].plot(u, v, '.w',markersize=1)
##    fareyImage[u,v] = 255
##    i = i + 1
##    if i == maxLines:
##        break
##
##maxLines = len(mLines)
##for i, mLine in enumerate(mLines):
##    u, v = mLine
##    ax[0].plot(u, v, '.r', markersize=1)
##    ax[1].plot(u, v, '.r',markersize=1)
##    fareyImage[u,v] = 255
##    i = i + 1
##    if i == maxLines:
##        break
###ax[0].set_title('Sampling (colour per line) for prime size:'+str(p))
###ax[1].set_title('Sampling (same colour per line) for prime size:'+str(p))
##ax[0].set_title('Sampling (colour per line) for dyadic size:'+str(M))
##ax[1].set_title('Sampling (same colour per line) for dyadic size:'+str(M))
###ax[0].set_xlim([0,M])
###ax[0].set_ylim([0,M])
###ax[1].set_xlim([0,M])
###ax[1].set_ylim([0,M])
##
###imageio.imsave("farey_image_"+str(p)+"_"+str(K)+".png", fareyImage)
##imageio.imsave("farey_image_"+str(M)+"_"+str(K)+".png", fareyImage)
##
##print("Non-zero elements: ", np.count_nonzero(fareyImage)/float((M*M))) 
##
##plt.show()
##

def fillImageSpace():
    N=512
    M=2*N
    centered = True

    ms = range(0, N)
    ss = range(0, N/2)

    powerSpect = np.zeros((M,M))
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))
    ax[0].imshow(powerSpect)
    ax[1].imshow(powerSpect)
    fareyImage = np.zeros_like(powerSpect)

    maxLines = len(ms)
    for i,m in enumerate(ms):
        u, v = radon.getSliceCoordinates2(m, powerSpect, centered, M)
        ax[0].plot(u, v, '.r', markersize=1)
        u, v = radon.getSliceCoordinates2(M-m, powerSpect, centered, M)
        ax[0].plot(u, v, '.r', markersize=1)    
        #ax[1].plot(u, v, '.r',markersize=1)
        fareyImage[u,v] = 255
        if i == maxLines:
            break

    maxLines = len(ss)
    for i,s in enumerate(ss):
        u, v = radon.getSliceCoordinates2(s, powerSpect, centered, M)
        ax[0].plot(u, v, '.r', markersize=1)
        ax[1].plot(u, v, '.r',markersize=1)
        u, v = radon.getSliceCoordinates2(M-s, powerSpect, centered, M)
        ax[0].plot(u, v, '.r', markersize=1)
        ax[1].plot(u, v, '.r',markersize=1)
        fareyImage[u,v] = 255
        if i == maxLines:
            break

    plt.show()

    print("Non-zero elements without holes: ", np.count_nonzero(fareyImage)/float(M*M) * 100)

    return

def createFractal(reduction, N, proportion):
    #parameters
    M = 2*N
    twoQuads = True
    angles, lengths = mojette.angleSet_Symmetric(N,N,1,True,50)
    perpAngle = farey.farey(1,0)
    angles.append(perpAngle)
    powerSpect = np.zeros((M,M))

    #compute lines
    centered = True
    mLines = []
    sLines = []
    mValues = []
    sValues = []
    pValues = []
    qValues = []
    for angle in angles:
        m, s, p, q, inv = farey.toFinite(angle, M)
        pValues.append(p)
        qValues.append(q)
        if m not in mValues and m < M:
            u, v = radon.getSliceCoordinates2(m, powerSpect, centered, M)
            mLines.append((u,v))
            mValues.append(m)
        
        #second quadrant
        if twoQuads:
            if m != 0 and m != M: #dont repeat these
                m = M-m
                if m not in mValues and m < M:
                    u, v = radon.getSliceCoordinates2(m, powerSpect, centered, M)
                    mLines.append((u,v))
                    mValues.append(m)
                    i = (len(mValues)+len(sValues))/float(M)
                    if i >= reduction*proportion:
                        break

    angles1, lengths1 = mojette.angleSet_Symmetric(N,N,1,True,100) #here
    perpAngle1 = farey.farey(1,0)
    angles1.append(perpAngle1)


    for angle in angles1:
        m, s, p, q, inv = farey.toFinite(angle, M)
        pValues.append(p)
        qValues.append(q)
        if s not in sValues and N+s < 0.75*M and N-s > 0:
            u, v = radon.getSliceCoordinates2(N-s, powerSpect, centered, M)
            sLines.append((u,v))
            u, v = radon.getSliceCoordinates2(N+s, powerSpect, centered, M)
            sLines.append((u,v))
            u, v = radon.getSliceCoordinates2(s, powerSpect, centered, M)
            sLines.append((u,v))
            sValues.append(N+s)
            sValues.append(N-s)
            sValues.append(s)
        
        #second quadrant
        if twoQuads:
            s = N/2-s            
            if s not in sValues and N+s < 0.75*M and N-s > 0:
                u, v = radon.getSliceCoordinates2(N-s, powerSpect, centered, M)
                sLines.append((u,v))
                u, v = radon.getSliceCoordinates2(N+s, powerSpect, centered, M)
                sLines.append((u,v))
                u, v = radon.getSliceCoordinates2(s, powerSpect, centered, M)
                sLines.append((u,v))
                sValues.append(N+s)
                sValues.append(N-s)
                sValues.append(s)

                i = (len(mValues)+len(sValues))/float(M)
                if i >= reduction:
                    break


    mu = len(mLines)
    print("Proportion of M:", (len(mLines)+len(sLines))/float(M))

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

    plt.gray()
    plt.tight_layout()

    maxLines = len(sLines+mLines)
    i = 0
    ax[0].imshow(powerSpect)
    ax[1].imshow(powerSpect)
    color=iter(cm.jet(np.linspace(0,1,maxLines+1)))
    fareyImage = np.zeros_like(powerSpect)
    fareyImage1 = np.zeros_like(powerSpect)
    for i, sLine in enumerate(sLines):
        u, v = sLine
        ax[1].plot(u, v, '.w',markersize=1)
        fareyImage[u,v] = 255
        i = i + 1
        if i == maxLines:
            break

    maxLines = len(mLines)
    for i, mLine in enumerate(mLines):
        u, v = mLine
        ax[0].plot(u, v, '.r', markersize=1)
        ax[1].plot(u, v, '.r',markersize=1)
        fareyImage[u,v] = 255
        fareyImage1[u,v] = 255
        i = i + 1
        if i == maxLines:
            break

    print("Non-zero elements with holes: ", np.count_nonzero(fareyImage1)/float((M*M)) * 100)
    print("Non-zero elements without holes: ", np.count_nonzero(fareyImage)/float((M*M)) * 100)

    print("Absolute difference percentage extra filled in is ", (np.count_nonzero(fareyImage)- np.count_nonzero(fareyImage1))/float((M*M)) *100)

    withHoles = np.count_nonzero(fareyImage1)/float((M*M)) * 100
    withoutHoles = np.count_nonzero(fareyImage)/float((M*M)) * 100

    percentage = (withoutHoles - withHoles)/float(withHoles) * 100

    print("Percentage difference percentage extra filled in is ", percentage)
    
    ax[0].set_title('Sampling (colour per line) for dyadic size:'+str(M))
    ax[1].set_title('Sampling (same colour per line) for dyadic size:'+str(M))
    imageio.imsave("farey_image_"+str(M)+"_"+".png", fareyImage)
    plt.show()

    lines = mLines + sLines

    return fareyImage, lines

def createFractal2(reduction, N, proportion):
    #parameters
    M = 2*N
    twoQuads = True
    angles, lengths = mojette.angleSet_Symmetric(N,N,1,True,50)
    perpAngle = farey.farey(1,0)
    angles.append(perpAngle)
    powerSpect = np.zeros((M,M))

    #compute lines
    centered = True
    mLines = []
    sLines = []
    mValues = []
    sValues = []
    pValues = []
    qValues = []
    for angle in angles:
        m, s, p, q, inv = farey.toFinite(angle, M)
        pValues.append(p)
        qValues.append(q)
        if m not in mValues and m < M:
            u, v = radon.getSliceCoordinates2(m, powerSpect, centered, M)
            mLines.append((u,v))
            mValues.append(m)
        
        #second quadrant
        if twoQuads:
            if m != 0 and m != M: #dont repeat these
                m = M-m
                if m not in mValues and m < M:
                    u, v = radon.getSliceCoordinates2(m, powerSpect, centered, M)
                    mLines.append((u,v))
                    mValues.append(m)
                    i = (len(mValues)+len(sValues))/float(M)
                    if i >= reduction*proportion:
                        break

    ss = []
    ss.append(M)
    ss.extend(range(0, N/2))

    maxLines = len(ss)
    for i,s in enumerate(ss):
        u, v = radon.getSliceCoordinates2(s, powerSpect, centered, M)
        sLines.append((u,v))
        sValues.append(s)
        i = (len(mValues)+len(sValues))/float(M)
        if i >= reduction:
            break

    mu = len(mLines)
    print("Proportion of M:", (len(mLines)+len(sLines))/float(M))

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

    plt.gray()
    plt.tight_layout()

    maxLines = len(sLines+mLines)
    i = 0
    ax[0].imshow(powerSpect)
    ax[1].imshow(powerSpect)
    color=iter(cm.jet(np.linspace(0,1,maxLines+1)))
    fareyImage = np.zeros_like(powerSpect)
    fareyImage1 = np.zeros_like(powerSpect)
    for i, sLine in enumerate(sLines):
        u, v = sLine
        ax[1].plot(u, v, '.w',markersize=1)
        fareyImage[u,v] = 1
        i = i + 1
        if i == maxLines:
            break

    maxLines = len(mLines)
    for i, mLine in enumerate(mLines):
        u, v = mLine
        ax[0].plot(u, v, '.r', markersize=1)
        ax[1].plot(u, v, '.r',markersize=1)
        fareyImage[u,v] = 1
        fareyImage1[u,v] = 1
        i = i + 1
        if i == maxLines:
            break

    print("Non-zero elements with holes: ", np.count_nonzero(fareyImage1)/float(M*M) * 100)
    print("Non-zero elements without holes: ", np.count_nonzero(fareyImage)/float(M*M) * 100)

    print("Absolute difference percentage extra filled in is ", (np.count_nonzero(fareyImage)- np.count_nonzero(fareyImage1))/float((M*M)) *100)

    withHoles = np.count_nonzero(fareyImage1)/float((M*M)) * 100
    withoutHoles = np.count_nonzero(fareyImage)/float((M*M)) * 100

    percentage = (withoutHoles - withHoles)/float(withHoles) * 100

    print("Percentage difference percentage extra filled in is ", percentage)
            
    ax[0].set_title('Sampling (colour per line) for dyadic size:'+str(M))
    ax[1].set_title('Sampling (same colour per line) for dyadic size:'+str(M))
    imageio.imsave("farey_image_"+str(M)+"_"+".png", fareyImage)
    plt.show()

    lines = mLines + sLines

    return fareyImage, lines

def createFractal3(reduction, N, proportion):
    #parameters
    M = 2*N
    twoQuads = True
    angles, lengths = mojette.angleSet_Symmetric(N,N,1,True,50)
    perpAngle = farey.farey(1,0)
    angles.append(perpAngle)
    powerSpect = np.zeros((M,M))

    #compute lines
    centered = True
    mLines = []
    sLines = []
    mValues = []
    sValues = []
    pValues = []
    qValues = []
    for angle in angles:
        m, s, p, q, inv = farey.toFinite(angle, M)
        pValues.append(p)
        qValues.append(q)
        if m not in mValues and m < M:
            u, v = radon.getSliceCoordinates2(m, powerSpect, centered, M)
            mLines.append((u,v))
            mValues.append(m)
        
        #second quadrant
        if twoQuads:
            if m != 0 and m != M: #dont repeat these
                m = M-m
                if m not in mValues and m < M:
                    u, v = radon.getSliceCoordinates2(m, powerSpect, centered, M)
                    mLines.append((u,v))
                    mValues.append(m)
                    i = (len(mValues)+len(sValues))/float(M)
                    if i >= 1:
                        break

    angles1, lengths1 = mojette.angleSet_Symmetric(N,N,1,True,100) #here
    perpAngle1 = farey.farey(1,0)
    angles1.append(perpAngle1)


    for angle in angles1:
        m, s, p, q, inv = farey.toFinite(angle, M)
        pValues.append(p)
        qValues.append(q)
        if s not in sValues and N+s < 0.75*M and N-s > 0:
            u, v = radon.getSliceCoordinates2(N-s, powerSpect, centered, M)
            sLines.append((u,v))
            u, v = radon.getSliceCoordinates2(N+s, powerSpect, centered, M)
            sLines.append((u,v))
            u, v = radon.getSliceCoordinates2(s, powerSpect, centered, M)
            sLines.append((u,v))
            sValues.append(N+s)
            sValues.append(N-s)
            sValues.append(s)
        
        #second quadrant
        if twoQuads:
            s = N/2-s            
            if s not in sValues and N+s < 0.75*M and N-s > 0:
                u, v = radon.getSliceCoordinates2(N-s, powerSpect, centered, M)
                sLines.append((u,v))
                u, v = radon.getSliceCoordinates2(N+s, powerSpect, centered, M)
                sLines.append((u,v))
                u, v = radon.getSliceCoordinates2(s, powerSpect, centered, M)
                sLines.append((u,v))
                sValues.append(N+s)
                sValues.append(N-s)
                sValues.append(s)

                i = (len(mValues)+len(sValues))/float(M)
                if i >= 1.5:
                    break


    length = 0
    #print("Proportion of M:", (len(mLines)+len(sLines))/float(M))

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

    plt.gray()
    plt.tight_layout()

    maxLines = len(sLines+mLines)
    i = 0
    ax[0].imshow(powerSpect)
    ax[1].imshow(powerSpect)
    color=iter(cm.jet(np.linspace(0,1,maxLines+1)))
    fareyImage = np.zeros_like(powerSpect)
    fareyImage1 = np.zeros_like(powerSpect)
    for i, sLine in enumerate(sLines):
        u, v = sLine
        ax[1].plot(u, v, '.w',markersize=1)
        fareyImage[u,v] = 255
        length = length + 1
        i = np.count_nonzero(fareyImage)/float((M*M))
        if i >= reduction*proportion:
            break

    maxLines = len(mLines)
    for i, mLine in enumerate(mLines):
        u, v = mLine
        ax[0].plot(u, v, '.r', markersize=1)
        ax[1].plot(u, v, '.r',markersize=1)
        fareyImage[u,v] = 255
        fareyImage1[u,v] = 255
        length = length + 1
        i = np.count_nonzero(fareyImage)/float((M*M))
        if i >= reduction:
            break


    print("Proportion of M:", (length/float(M)))

    print("Non-zero elements with holes: ", np.count_nonzero(fareyImage1)/float((M*M)) * 100)
    print("Non-zero elements without holes: ", np.count_nonzero(fareyImage)/float((M*M)) * 100)

    print("Percentage extra filled in is ", (np.count_nonzero(fareyImage)- np.count_nonzero(fareyImage1))/float((M*M)) *100)

    withHoles = np.count_nonzero(fareyImage1)/float((M*M)) * 100
    withoutHoles = np.count_nonzero(fareyImage)/float((M*M)) * 100

    percentage = (withoutHoles - withHoles)/float(withHoles) * 100

    print("Percentage extra filled in is ", percentage)
    
    ax[0].set_title('Sampling (colour per line) for dyadic size:'+str(M))
    ax[1].set_title('Sampling (same colour per line) for dyadic size:'+str(M))
    imageio.imsave("farey_image_"+str(M)+"_"+".png", fareyImage)
    plt.show()

    lines = mLines + sLines

    return fareyImage, lines

def createFractal4(reduction, N, proportion):
    #parameters
    M = 2*N
    twoQuads = True
    angles, lengths = mojette.angleSet_Symmetric(N,N,1,True,50)
    perpAngle = farey.farey(1,0)
    angles.append(perpAngle)
    powerSpect = np.zeros((M,M))

    #compute lines
    centered = True
    mLines = []
    sLines = []
    mValues = []
    sValues = []
    pValues = []
    qValues = []
    for angle in angles:
        m, s, p, q, inv = farey.toFinite(angle, M)
        pValues.append(p)
        qValues.append(q)
        if m not in mValues and m < M:
            u, v = radon.getSliceCoordinates2(m, powerSpect, centered, M)
            mLines.append((u,v))
            mValues.append(m)
        
        #second quadrant
        if twoQuads:
            if m != 0 and m != M: #dont repeat these
                m = M-m
                if m not in mValues and m < M:
                    u, v = radon.getSliceCoordinates2(m, powerSpect, centered, M)
                    mLines.append((u,v))
                    mValues.append(m)
                    i = (len(mValues)+len(sValues))/float(M)
                    if i >= 1:
                        break

    ss = []
    ss.append(M)
    ss.extend(range(0, N/2))

    maxLines = len(ss)
    for i,s in enumerate(ss):
        u, v = radon.getSliceCoordinates2(s, powerSpect, centered, M)
        sLines.append((u,v))
        sValues.append(s)
        i = (len(mValues)+len(sValues))/float(M)
        if i >= 1.5:
            break

    length = 0

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

    plt.gray()
    plt.tight_layout()

    maxLines = len(sLines+mLines)
    i = 0
    ax[0].imshow(powerSpect)
    ax[1].imshow(powerSpect)
    color=iter(cm.jet(np.linspace(0,1,maxLines+1)))
    fareyImage = np.zeros_like(powerSpect)
    fareyImage1 = np.zeros_like(powerSpect)
    for i, sLine in enumerate(sLines):
        u, v = sLine
        ax[1].plot(u, v, '.w',markersize=1)
        fareyImage[u,v] = 1
        length = length + 1
        i = np.count_nonzero(fareyImage)/float((M*M))
        if i >= reduction*proportion:
            break

    maxLines = len(mLines)
    for i, mLine in enumerate(mLines):
        u, v = mLine
        ax[0].plot(u, v, '.r', markersize=1)
        ax[1].plot(u, v, '.r',markersize=1)
        fareyImage[u,v] = 1
        fareyImage1[u,v] = 1
        length = length + 1
        i = np.count_nonzero(fareyImage)/float((M*M))
        if i >= reduction:
            break

    print("Proportion of M:", (length/float(M)))

    print("Non-zero elements with holes: ", np.count_nonzero(fareyImage1)/float((M*M)) * 100)
    print("Non-zero elements without holes: ", np.count_nonzero(fareyImage)/float((M*M)) * 100)

    print("Absolute difference percentage extra filled in is ", (np.count_nonzero(fareyImage)- np.count_nonzero(fareyImage1))/float((M*M)) *100)

    withHoles = np.count_nonzero(fareyImage1)/float((M*M)) * 100
    withoutHoles = np.count_nonzero(fareyImage)/float((M*M)) * 100

    percentage = (withoutHoles - withHoles)/float(withHoles) * 100

    print("Percentage difference percentage extra filled in is ", percentage)
            
    ax[0].set_title('Sampling (colour per line) for dyadic size:'+str(M))
    ax[1].set_title('Sampling (same colour per line) for dyadic size:'+str(M))
    imageio.imsave("farey_image_"+str(M)+"_"+".png", fareyImage)
    plt.show()

    lines = mLines + sLines

    return fareyImage, lines


fillImageSpace()

N=512
M=2*N
fractal, lines = createFractal(0.2, N, 0.7)

print(fractal)

#measurements = ski.measure.regionprops(fractal.astype(int), 'area')

plt.figure()
plt.imshow(fractal)
plt.title('Greyscale fractal for dyadic size:'+str(M))
plt.show()

N=512
M=2*N
fractal, lines = createFractal2(0.2, N, 0.7)

plt.figure()
plt.imshow(fractal)
plt.title('Greyscale fractal for dyadic size:'+str(M))
plt.show()

N=512
M=2*N
fractal, lines = createFractal3(0.2, N, 0.7)

plt.figure()
plt.imshow(fractal)
plt.title('Greyscale fractal for dyadic size:'+str(M))
plt.show()

N=512
M=2*N
fractal, lines = createFractal4(0.2, N, 0.7)

plt.figure()
plt.imshow(fractal)
plt.title('Greyscale fractal for dyadic size:'+str(M))
plt.show()


# -*- coding: utf-8 -*-
"""
Process 2D slices and produce turbulent artefacts

Created on Wed Nov 21 10:28:15 2018

@author: uqscha22
"""
#get list of images
import filenames
#load modules for arrays and nifti file support
import numpy as np
import nibabel as nib
import finite
import scipy.fftpack as fftpack
import pyfftw

#plot slices responsible for reconstruction
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm 

# Monkey patch in fftn and ifftn from pyfftw.interfaces.scipy_fftpack
fftpack.fft2 = pyfftw.interfaces.scipy_fftpack.fft2
fftpack.ifft2 = pyfftw.interfaces.scipy_fftpack.ifft2
fftpack.fft = pyfftw.interfaces.scipy_fftpack.fft
fftpack.ifft = pyfftw.interfaces.scipy_fftpack.ifft

# Turn on the cache for optimum performance
pyfftw.interfaces.cache.enable()

N = 256
K = 2.4
path = "slices/" #3D volumes
outpath = "slices_artefact/"
output_prefix = "case_"
caseIndex = 0

#setup fractal
#lines, angles, mValues, fractal, oversampling = finite.finiteFractal(N, K, sortBy='Euclidean', twoQuads=True)
fractal, lines = createFractal(1, 128, 0.7)
mu = len(lines)
print("Number of finite lines:", mu)
print("Number of finite points:", mu*(N-1))

imageList, caseList = filenames.getSortedFileListAndCases(path, caseIndex, "*.nii.gz", True)
imageList, sliceList = filenames.getSortedFileListAndCases(path, caseIndex+1, "*.nii.gz", True)
#print(imageList)
#print(caseList)

def show_slices(slices):
    """ Function to display row of image slices """
    fig, axes = plt.subplots(1, len(slices))
    for i, slice in enumerate(slices):
        axes[i].imshow(slice.T, cmap="gray", origin="lower")

#process each 3D volume
count = 0
for image, case, sliceIndex in zip(imageList, caseList, sliceList):
    img = nib.load(image)
    print("Loaded", image)

    #get the numpy array version of the image
    data = img.get_data() #numpy array without orientation
    fdata = img.get_fdata()
    lx, ly, lz = data.shape
    print("Image shape:", data.shape)

##    slice_0 = fdata[26, :, :]
##    slice_1 = fdata[:, 30, :]
##    slice_2 = fdata[:, :, 0]
##
##    fig, axes = plt.subplots(1, 3)
##    axes[0].imshow(slice_0.T, cmap="gray", origin="lower")
##    axes[1].imshow(slice_1.T, cmap="gray", origin="lower")
##    axes[2].imshow(slice_2.T, cmap="gray", origin="lower")
##        
##    plt.suptitle("Center slices for EPI image")  # doctest: +SKIP
##    plt.show()

    slice0 = fdata[:, :, 0]
    slice0 = np.swapaxes(slice0, 0, 1)
    fig, ax = plt.subplots(1, 2)
    ax[0].imshow(slice0, cmap="gray", origin="lower")
    
    #pad
    mid = int(N/2.0)
    midx = int(lx/2.0+0.5)
    midy = int(ly/2.0+0.5)
    newLengthX1 = mid - midx
    newLengthX2 = mid + midx
    newLengthY1 = mid - midy
    newLengthY2 = mid + midy
    newImage = np.zeros((N,N))
#    imageio.imcrop(data, N, m=0, center=True, out_dtype=np.uint32)
    newImage[newLengthX1:newLengthX2, newLengthY1:newLengthY2] = data[:,:,0]
    
    #2D FFT
    kSpace = fftpack.fft2(newImage) #the '2' is important
#    fftkSpaceShifted = fftpack.fftshift(kSpace)
    kSpace *= fractal
    artefactImage = fftpack.ifft2(kSpace) #the '2' is important
    artefactImage = np.real(artefactImage)

    #artefactImage = np.fliplr(artefactImage)
    #artefactImage = np.flipud(artefactImage)
    artefactImage = np.swapaxes(artefactImage, 0, 1)

    ax[1].imshow(artefactImage, cmap="gray", origin="lower")
    plt.show()
 
    slice = nib.Nifti1Image(artefactImage, np.eye(4))
    outname = outpath + output_prefix + str(case).zfill(3) + "_slice_" + str(sliceIndex) + ".nii.gz"
    slice.to_filename(outname)
    count += 1
    
#    break
print("Total", count, "processed")






