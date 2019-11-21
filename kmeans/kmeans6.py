import numpy as np
from sklearn.cluster import KMeans
import time
import os

def get_data_list(file_path):
    file_data=open(file_path,'r+')
    data_list=[]
    for line in file_data:
        line=line.strip('\n')
        data_list.append(line)
    return data_list

def get_vgg_arr(data_list):
    image_info = []
    image_dir = '/Users/tangyubao/cmr-yzq/data/eng-wiki/image_vgg19_pool5/'
    for file_name in data_list:
        file_path = os.path.join(image_dir, file_name)
        one_image = np.load(file_path)
        image_info.append(one_image)
    train_image_arr = np.array(image_info)  # (image_num,49,512)
    image_num, forty_nine, five_one_two = train_image_arr.shape
    all_image_arr = np.reshape(train_image_arr, newshape=(image_num * forty_nine, five_one_two))
    # all image arr is patch matrix
    return image_num,all_image_arr


#build graph
def build_graph(k,neigh_idx,neigh_num):
    start=time.clock()
    print('building graph...')
    graph=np.zeros((k,k),dtype=np.int)
    for i in range(k):
      for j in range(neigh_num):
        graph[i][neigh_idx[i][j]]=1
    print('graph.shape:',graph.shape)
    end=time.clock()
    print('build graph cost time:',(end-start)*1000,'ms')
    np.save('image_graph.npy',graph)

    graph_check=np.sum(graph,axis=1)
    for i in range(k):
        print(i,'--',graph_check[i])

#build feature matrix
def build_feature_file(image_arr,image_num,data_list):
    #prepare
    start = time.clock()
    print('building feature file...')
    all_patch_num=image_arr.shape[0]
    one_image_patch=49
    image_cos_dis=[]
    for i in range(all_patch_num):
      dot=np.dot(all_image_arr[i],cluster_cent.T)
      denom=np.linalg.norm(all_image_arr[i])*np.linalg.norm(cluster_cent,axis=1)
      np.seterr(divide='ignore',invalid='ignore')
      cos=dot/denom
      zero_idx=np.where(denom==0)
      cos[zero_idx]=0
      sim=0.5+0.5*cos
      image_cos_dis.append(sim)
    # print('dot[0]:',dot[0])
    image_cos_dis=np.array(image_cos_dis)
    image_sortIdx=np.argsort(-image_cos_dis,axis=1)
    image_sortIdx=image_sortIdx[:,:1]
    # print('image_cos_dis.shape:',image_cos_dis.shape)
    # print('image_sortIdx.shape:',image_sortIdx.shape)


    #generate feature file
    feature_dir='eng-wiki/image_feature/'
    feature_matrix=np.zeros((image_num,k),dtype=np.int)
    for i in range(all_patch_num):
        feature_matrix[int(i/one_image_patch)][image_sortIdx[i]]+=1
    #feature_matrix=np.expand_dims(feature_matrix,axis=2)
    print('feature matrix shape:',feature_matrix.shape)
    for i in range(image_num):
       # image_name='image_feature_file_'+data_list[i].split('_',3)[-1]
        image_path=os.path.join(feature_dir,data_list[i])
        np.save(image_path,np.expand_dims(feature_matrix[i],axis=2))
    end = time.clock()
    print('build feature file cost time:', (end - start) * 1000, 'ms')


train_file_path='/Users/tangyubao/cmr-yzq/data/eng-wiki/image_vgg19_pool5_train.txt'
val_file_path='/Users/tangyubao/cmr-yzq/data/eng-wiki/image_vgg19_pool5_val.txt'
train_list=get_data_list(train_file_path)
val_list=get_data_list(val_file_path)

# image_arr=(image_num * forty_nine, five_one_two)
train_image_num,train_image_arr=get_vgg_arr(train_list)
val_image_num,val_image_arr=get_vgg_arr(val_list)

all_image_arr=np.concatenate((train_image_arr,val_image_arr),axis=0)
# print('train_arr.shape:',train_image_arr,'val_arr.shape:',val_image_arr,'all_image_arr.shape:',all_image_arr)

iteration=200
k=200
model=KMeans(n_clusters=k,n_jobs=4,max_iter=iteration)
model.fit(all_image_arr)
cluster_cent=model.cluster_centers_
# print('model.labels_.shape',model.labels_.shape)
# print('model.labels_',model.labels_)
# print('cluster_cent.shape:',cluster_cent.shape)

#compute cosine distance among k cluster centers
cos_dis=[]
neigh_num=8
for i in range(k):
  the_cluster=cluster_cent[i]
  dot=np.dot(the_cluster,cluster_cent.T)
  denom=np.linalg.norm(the_cluster)*np.linalg.norm(cluster_cent,axis=1)
  cos=dot/denom
  sim=0.5+0.5*cos
  cos_dis.append(sim)
cos_dis=np.array(cos_dis)
cDis_sortIdx=np.argsort(-cos_dis)
neigh_idx=cDis_sortIdx[:,:neigh_num]
np.save('neigh.npy',neigh_idx)

# print('cos_dis.shape:',cos_dis.shape)
print('neigh_idx.shape:',neigh_idx.shape)
# print(neigh_idx[0])

build_graph(k,neigh_idx,neigh_num)
# build_feature_file(train_image_arr,train_image_num,train_list)
# build_feature_file(val_image_arr,val_image_num,val_list)


