

# Gsoc 2019
# Human history and data visualization

# selection test :
Write a program in python that does the following:

- Imports the genotype data in VCF and population description files (suggested package: scikit-allel).
- Dimensionally reduces the genotype data using principal components analysis and uniform manifold approximation and projection (there are libraries for this)
- Outputs a file containing coordinates of the low dimensional projections
- Outputs a 2D plot, which is coloured by the variables in the panel file and labelled using full variable names in the tsv file
- Outputs a log containing the random seeds used to generate coordinates, the program's run-time, versions of all packages used, verbose output of methods used, time stamps, and all parameters - - specified (results should be reproducible)
- All outputs should have a unique ID connecting them to the log file

# Result :
- The output files from the file are pca.npz,umap.npz,my1.log, which are the coordinates of the low dimensional projections of pca , umap and log file respectively.
- The main file is the selection_test.ipynb which can be run in google colab to get the same results.
- The projections of pca, umap can be seen in the ipynb output codes : 7,8,9,10.

# data conversion time: 288.5372965335846 sec 
# data load time: 0.002002716064453125 sec
# PCA time: 10.878305673599243 sec
# umap time: 0.002002716064453125 sec
# total program time: 561.180104970932 sec

# Why this project ?
I have been taking part in a lot of online and off-line hackathons in the past 2 years, which include Machine hack-predict the beer score, where I was placed 7th, Axis bank AI hackathon (National hackathon) where I was part of top 23 teams and I presented a PoC paper in IEEE CCEM Bangalore 2018 and got 3rd place. During this entire journey of machine learning, I always wondered what would let me visualize these high dimensional data and I knew for a fact that techniques like PCA could help me in this, but I never got time to learn them. Now due to this project, I am very excited to explore more in this domain and hope to make a good contribution to the open source community by helping them visualize genotype data in a simple language like python. I was overwhelmed looking at how UMAP gave me clear cut differences in the group than PCA and I am sure in this journey I will find more such moments.

# Conclusion :
Clearly UMAP takes a lot less time than PCA and gives better results than PCA.