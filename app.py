import streamlit as st
import plotly.express as px
import pandas as pd
import time
import numpy as np
def turn_around_time(arrival,finish):
  """
  Provide arrival time and finish time as array inputs returns 
  """
  turn_around_time=[]
  for x in range(len(arrival)):
    turn_around_time.append(finish[x]-arrival[x])
  return turn_around_time

def wait_time(turn_around,burst):
  """
  provide array input and will produce array as output
  """
  wait=[]
  for x in range(len(burst)):
    wait.append(turn_around[x]-burst[x])
  return wait

def make_dataframe(process,start,burst,finish,turn_around,wait):
  """
  provide the arrays for all attributes and converted dataframe will be returned
  """
  df=pd.DataFrame({"Process":process,'Arrival Time':start,"Burst Time":burst,'Completion Time':finish,'Turn Around Time':turn_around,'Waiting Time':wait}).sort_values(by ='Process' )
  return df

def fcfs(process):
  time=0 #variable to keep track of time passed
  gant=[] # arrAY TO STORE THE dictionaries to make the gaant chart
  for x in process:
    if x[1]>time:  
      gant.append(dict(Task='Empty',Start=time,Finish=x[1])) #add if no process waiting 
      time=x[1] 
    gant.append(dict(Task=x[0],Start=time,Finish=time+x[2])) # add process to timeline 
    
    time+=x[2] # new time= prev_time+burst time of process run
  finish=[-1 for x in range(len(process))] 
  arrival=[]
  burst=[]
  process_names=[]
  for x in process:
    process_names.append(x[0])
    arrival.append(x[1])
    burst.append(x[2])
  for x in gant:
    if x["Task"]=='Empty':
      continue
    s=process_names.index(x['Task'])
    finish[s]=x['Finish']
  turn_around=turn_around_time(arrival,finish)
  wait=wait_time(turn_around,burst)
  df=make_dataframe(process_names,arrival,burst,finish,turn_around,wait)    
  return gant,df #return gantt chart and the dataframe 


def sjf(process):
  time=0 #cPU time
  gant=[]
  queue=[]
  finish=[-1 for z in range(len(process))] 
  arrival=[]
  burst=[]
  process_names=[]
  for x in process:
    process_names.append(x[0])
    arrival.append(x[1])
    burst.append(x[2])


  while process or queue:
    if len(queue)==0:
      queue.append(process.pop(0))
      if queue[0][1]>time:
        gant.append(dict(Task='Empty',Start=time,Finish=queue[0][1],Priority=0))
        time=queue[0][1]
    if process:
      while process[0][1]==time:
        queue.append(process.pop(0))
    queue.sort(key= lambda x: x[2])
    temp=queue.pop(0)
    gant.append(dict(Task=temp[0],Start=time,Finish=time+temp[2]))
    time+=temp[2]
    if process:
      while process[0][1]<=time:
        queue.append(process.pop(0))
        if not process:
          break

  
  temp=[]
  for x in gant[::-1]:
    if x['Task']!="Empty" and x['Task'] not in temp:
      temp.append(x['Task'])
      s=process_names.index(x['Task'])
      finish[s]=x['Finish']
  turn_around=turn_around_time(arrival,finish)
  wait=wait_time(turn_around,burst)
  df=make_dataframe(process_names,arrival,burst,finish,turn_around,wait)    
  return gant,df

def priority_scheduling(process):
  time=0
  queue=[]
  gant=[]
  arrival=[]
  process_name=[]
  finish=[-1 for x in range(len(process))]
  burst=[]
  for x in process:
    arrival.append(x[1])
    burst.append(x[2])
    process_name.append(x[0])
  while len(process)!=0 or len(queue)!=0:
    if len(queue)==0:
      queue.append(process.pop(0))
      if queue[0][1]>time:
        gant.append(dict(Task='Empty',Start=time,Finish=queue[0][1],Priority=0))
        time=queue[0][1]
    if process:
      while process[0][1]==time:
        queue.append(process.pop(0))
      
    queue.sort(key= lambda x:(x[3],x[0]))
    temp=queue.pop()
    gant.append(dict(Task=temp[0],Start=time,Finish=time+temp[2],Priority=temp[3]))
    time+=temp[2]
    if process:
      while process[0][1]<=time:
        queue.append(process.pop(0))
        if not process:
          break
  
  temp=[]
  for x in gant[::-1]:
    if x['Task']!="Empty" and x['Task'] not in temp:
      temp.append(x['Task'])
      s=process_name.index(x['Task'])
      finish[s]=x['Finish']
  turn_around=turn_around_time(arrival,finish)
  wait=wait_time(turn_around,burst)
  df=make_dataframe(process_name,arrival,burst,finish,turn_around,wait)
  return gant,df
    

def round_robin(pro,time_quanta):
  temp_process=pro.copy()
  time=0
  queue=[]
  gant=[]
  arrival=[]
  process_name=[]
  finish=[-1 for x in range(len(temp_process))]
  burst=[]
  for x in pro:
    arrival.append(x[1])
    burst.append(x[2])
    process_name.append(x[0])
  while len(temp_process)!=0 or len(queue)!=0:
    if len(queue)==0: #no proccesse have arrived on given cpu time
      queue.append(temp_process.pop(0)) # adding the first process that arrives 
      if queue[0][1]>time:  #if it's arrival time is larger than cpu_time then CPU will be empty from time to arrival_time of process
        gant.append(dict(Task='Empty',Start=time,Finish=queue[0][1]))
        time=queue[0][1]
    temp=queue.pop(0)
    if temp[2]<=time_quanta:
      gant.append(dict(Task=temp[0],Start=time,Finish=time+temp[2]))
      time+=temp[2]
      temp[2]=0
    else:
      gant.append(dict(Task=temp[0],Start=time,Finish=time+time_quanta))
      time+=time_quanta
      temp[2]-=time_quanta
    for x in temp_process:
      if x[1]<=time:
        queue.append(temp_process.pop(0))
    if temp[2]!=0:
      queue.append(temp)
  temp=[]
  for x in gant[::-1]:
    if x['Task']!="Empty" and x['Task'] not in temp:
      temp.append(x['Task'])
      s=process_name.index(x['Task'])
      finish[s]=x['Finish']
  turn_around=turn_around_time(arrival,finish)
  wait=wait_time(turn_around,burst)
  df=make_dataframe(process_name,arrival,burst,finish,turn_around,wait)
  return gant,df



def make_gantt_chart(process,algo,time_quanta):
  process.sort(key =lambda x:x[1]) #sorting process by arrival time
  if algo=='FCFS':
    gantt,details=fcfs(process)
  elif algo=='SJF':
    gantt,details=sjf(process)
  elif algo=='Priority Scheduling':
    gantt,details=priority_scheduling(process)
  else: 
    gantt,details=round_robin(process,time_quanta)
  #gantt is a list of dictionaries 
  gantt.sort(key = lambda gantt: gantt['Task'])
  fig = px.timeline(gantt, x_start="Start", x_end="Finish", y="Task") 
  fig.update_yaxes(autorange="reversed") 
  fig.layout.xaxis.type = 'linear'
  delta=[] # to plot integers instead of dates on x-axis
  for x  in gantt:
    delta.append(x['Finish']-x['Start'])
  fig.data[0].x = delta  
  return fig,details


def app_layout():
  algorithms=['FCFS', 'SJF', 'Round Robin',"Priority Scheduling"]
  st.set_page_config(layout="wide")
  st.title("CPU Scheduling Algorithms")
  algo=st.multiselect( 'Select Algorithm',options=algorithms,default="FCFS")  # Choose the algorithm
  time_quanta=0 # a variable to store time_quantum for round robin
  if 'FCFS' in algo:
    st.subheader("FCFS")
    st.write("FCFS is an operating system scheduling algorithm that executes queued request and processes arrives in their order. The name itself suggest that the process which arrive first gets executed first. The process which request the CPU first, get the CPU allocation first. Usually it is managed by FIFO queue. It is simplest form of CPU scheduling algorithm.")
    st.subheader("Advantages")
    st.write("It supports non-preemptive and pre-emptive scheduling algorithm. It is easy to implement and use.")
    st.subheader("DisAdvantages")
    st.write("The average waiting time is very high. There is no ideal technique for time-sharing systems. It is not very efficient.")
  if 'SJF'in algo:
    st.subheader("SJF")
    st.write("SJF scheduling algorithm, schedules the processes according to their burst time. The process having the smallest execution time is chosen for the next execution. It reduces the average waiting time for other processes awaiting execution. It is associated with each job as a unit of time to complete.It can improve process throughput by making sure that shorter jobs are executed first, hence possibly have a short turnaround time.")
    st.subheader("Advantages")
    st.write("Works for both preemptive and non-preemptive.Frequently used for long term scheduling.Reduces The average waiting time over FIFO algorithm.This method is helpful for batch-type processing, where waiting for jobs to complete is not critical.Optimal with regard to average turn around time.")
    st.subheader("DisAdvantages")
    st.write("SJF can’t be implemented for CPU scheduling for the short term. It is because there is no specific method to predict the length of the upcoming CPU burst.Requires knowledge of how long a process or job will run.It leads to the starvation that does not reduce average turnaround time.It is hard to know the length of the upcoming CPU request.")
  if 'Round Robin' in algo:
    st.subheader("Round Robin")
    st.write("RR is a CPU scheduling algorithm where each process is assigned a fixed time slot in a cyclic way, where each process gets equal share in time processing. RR is a hybrid model which is clock-driven. In this, CPU is shifted to the next process after fixed interval time, which is called time quantum/time slice. Time slice should be minimum, which is assigned for a specific task that needs to be processed. However, it may differ OS to OS.")
    st.subheader("Advantages")
    st.write("A round-robin scheduler generally employs time-sharing, giving each job a time slot or quantum. Each process get a chance to reschedule after a particular quantum time in this scheduling. All the jobs get a fair allocation of CPU.It deals with all process without any priority.This scheduling method does not depend upon burst time. That’s why it is easily implementable on the system.It gives the best performance in terms of average response time.")
    st.subheader("DisAdvantages")
    st.write("Gantt chart seems to come too big (if quantum time is less for scheduling.For Example:1 ms for big scheduling.)There is low throughput and context switches.Lower time quantum results in higher the context switching overhead in the system.Finding a correct time quantum is a quite difficult task in this system.If slicing time of OS is low, the processor output will be reduced.")
    time_quanta=st.number_input(label="Time Quantum",min_value=1, max_value=10,step=1,key="RR_quantum") #input for time quantum
  
  #the process is limited to 8 because otherwise the integers are not visible in the input box
  num = st.number_input('Number of processes', min_value=1, max_value=8, value=5, step=1) #choose number of process
  process=[] # array to store data  about the processes
  
  cols=st.columns(num) #creating columns for input
  #might change column structure later so that input for more process can be taken
  for i,x in enumerate(cols):
    with x:
      st.write('Process {}'.format(i))
      temp=['P{}'.format(i),0,0]
      temp[1]=st.number_input(label="Arrival Time",min_value=0, max_value=100, value=i, step=1,key="AT{}".format(i))
      temp[2]=st.number_input(label="Burst Time",min_value=1, max_value=100, value=i+1, step=1,key="BT{}".format(i))
      if 'Priority Scheduling' in algo:
        temp.append(st.number_input(label="Priority",min_value=1, max_value=10, value=i+1, step=1,key="Priority{}".format(i)))
      process.append(temp)
  # code will execute when the below button is prsses to avoid to much processing as streamlit reloads whenever any input value changes
  

  submit=st.button(label='Execute')
  if submit:
    for algorithm in algo:
      st.title(algorithm)
      pro=process.copy()
      #details contains the info such as AT,BT,TAT,WT
      #timeline is a gantt chart for all processes
      timeline,details=make_gantt_chart(pro,algorithm,time_quanta) 
      col1,col2=st.columns(2)
      with col1:
        st.write("Scheduling result")
        st.write(details)
      with col2:
        st.write("Gantt Chart")
        st.plotly_chart(timeline)          
      col1,col2=st.columns(2)
      col1.metric(label="Average Turn Around Time", value=round(details['Turn Around Time'].mean(),2))
      col2.metric(label='Average waiting time',value=round(details['Waiting Time'].mean(),2))
      

if __name__=='__main__':
  app_layout()
