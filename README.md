<h1>Scheduling-algo-simulator</h1>

<p>
Scheduling algorithms decide in which order should the processes be scheduled on the CPU. The scheduling algorithms differe based on the factors on which the use to decide the next scheduled process. There are static and dynamic prediction algorithms. 
</p>

<h2>Summary</h2>

<p>Project is based on CPU scheduling algorithm. The algorithm FCFS, SJF, RR, Priority Scheduling are implemented and obtained their gantt chart waiting time, execution time, and various other insights.</p>

<h2>Let's have a look!!</h2>

<h2>Types of scheduling algorithms</h2>
<ol>
    <li>
        <h3>Static Prediction</h3>
        <p>The Burst time is predicted using the attributes of the process, i.e. the Process Size and Process Type</p>
        <p><b>Process Size: </b> The algorithms uses the size of the process(kB) to find the burst time. The prediction is done through the knowledge the algorithm has about the previous processes, i.e. their sizes and their actual burst times. </p>
        <p><b>Process Type: </b> There are different types of processes inside an Operating system such as User processes, interactive processes and system processes.</p>
    </li>
    <li>
        <h3>Dynamic Prediction</h3>
        <p>The Burst time is predicted using the burst times of previously scheduled processes.</p>
        <p><b>Moving Average: </b> The algorithms predicts the burst time to be the average of the past k processes. The value of k can be varied which will result in different predictions.</p>
        <p><b>Exponential Average</b></p>
    </li>
</ol>

<h2>Now the algorithms we implemented are:</h2>

<ol>
    <li>
        <h2>FCFS(First Come First Serve)</h2>
        <p>FCFS is an operating system scheduling algorithm that executes queued request and processes arrives in their order. The name itself suggest that the process which arrive first gets executed first. The process which request the CPU first, get the CPU allocation first. Usually it is managed by FIFO queue. It is simplest form of CPU scheduling algorithm.</p>
        <ul type="square">
            <li><h3>Advantage</h3></li>
            <ul type="circle">
                <li>It supports non-preemptive and pre-emptive scheduling algorithm.</li>
                <li>It is easy to implement and use.</li>
            </ul>   
            <li><h3>Disadvantage</h3></li>
            <ul type="circle">
                <li>The average waiting time is very high.</li>
                <li>There is no ideal technique for time-sharing systems.</li>
                <li>It is not very efficient.</li>
            </ul>
            <li><h3>Example</h3></li> 
            <img src= "https://github.com/NidhayPancholi/Scheduling-algo-simulator/blob/main/FCFS.png">
            <li><h3>Implementation</h3></li>
            <ol>
                <li>Input the processes along with their burst time (bt).</li>
                <li>Find waiting time (wt) for all processes.</li>
                <li>As first process that comes need not to wait so waiting time for process 1 will be 0 i.e. wt[0] = 0.</li>
                <li>Find waiting time for all other processes i.e. for process i -> wt[i] = bt[i-1] + wt[i-1].</li>
                <li>Find turnaround time = waiting_time + burst_time for all processes.</li>
                <li>Find average waiting time total_waiting_time / no_of_processes.</li>
                <li>Similarly, find average turnaround time= total_turn_around_time / no_of_processes.</li>
            </ol>
        </ul>
    </li>
    <li>
        <h2>SJF(Shortest Job First)</h2>
        <p>SJF scheduling algorithm, schedules the processes according to their burst time. The process having the smallest execution time is chosen for the next execution. It reduces the average waiting time for other processes awaiting execution. It is associated with each job as a unit of time to complete.It can improve process throughput by making sure that shorter jobs are executed first, hence possibly have a short turnaround time.</p>
        <ul type="square">
            <li><h3>Advantage</h3></li>
            <ul type="circle">
                <li>Works for both preemptive and non-preemptive.</li>
                <li>Frequently used for long term scheduling.</li>
                <li>Reduces the average waiting time over FIFO algorithm.</li>
                <li>This method is helpful for batch-type processing, where waiting for jobs to complete is not critical.</li>
                <li>Optimal with regard to average turn around time.</li>
            </ul>
            <li><h3>Disadvantage</h3></li>
            <ul type="circle">
                <li>SJF can’t be implemented for CPU scheduling for the short term. It is because there is no specific method to predict the length of the upcoming CPU burst.</li>
                <li>Requires knowledge of how long a process or job will run.</li>
                <li>It leads to the starvation that does not reduce average turnaround time.</li>
                <li>It is hard to know the length of the upcoming CPU request.</li>
            </ul>
            <li><h3>Example</h3></li>
            <img src="https://github.com/NidhayPancholi/Scheduling-algo-simulator/blob/main/SJF.jpg">
        </ul>
    </li>
    <li>
        <h2>Round Robin</h2>
        <p>RR is a CPU scheduling algorithm where each process is assigned a fixed time slot in a cyclic way, where each process gets equal share in time processing. RR is a hybrid model which is clock-driven. In this, CPU is shifted to the next process after fixed interval time, which is called time quantum/time slice. Time slice should be minimum, which is assigned for a specific task that needs to be processed. However, it may differ OS to OS.</p>
        <ul type="square">
            <li><h3>Advantage</h3></li>
            <ul type="circle">
                <li>A round-robin scheduler generally employs time-sharing, giving each job a time slot or quantum.</li>
                <li>Each process get a chance to reschedule after a particular quantum time in this scheduling.</li>
                <li>All the jobs get a fair allocation of CPU.</li>
                <li>It deals with all process without any priority.</li>
                <li>This scheduling method does not depend upon burst time. That’s why it is easily implementable on the system.</li>
                <li>It gives the best performance in terms of average response time.</li>
            </ul>
            <li><h3>Disadvantage</h3></li>
            <ul type="circle">
                <li>Gantt chart seems to come too big (if quantum time is less for scheduling.For Example:1 ms for big scheduling.)</li>
                <li>There is low throughput and context switches.</li>
                <li>Lower time quantum results in higher the context switching overhead in the system.</li>
                <li>Finding a correct time quantum is a quite difficult task in this system.</li>
                <li>If slicing time of OS is low, the processor output will be reduced.</li>
            </ul>
            <li><h3>Example</h3></li>
            <img src="https://github.com/NidhayPancholi/Scheduling-algo-simulator/blob/main/round-robin-1.jpg">
            </ul>    
    </li>
    <li>
        <h2>Priority Scheduling</h2>
        <p>Priority Scheduling is a method of scheduling processes that is based on priority. In this algorithm, the scheduler selects the tasks to work as per the priority. The processes with higher priority should be carried out first, whereas jobs with equal priorities are carried out on a round-robin or FCFS basis. Priority depends upon memory requirements, time requirements, etc.</p>
         <ul type="square">
            <li><h3>Advantage</h3></li>
            <ul type="circle">
                <li>Processes are executed on the basis of priority so high priority does not need to wait for long which saves time</li>
                <li>Easy to use scheduling method</li>
                <li>Suitable for applications with fluctuating time and resource requirements.</li>
                <li>This method provides a good mechanism where the relative important of each process may be precisely defined.</li>
            </ul>
            <li><h3>Disadvantage</h3></li>
            <ul type="circle">
                <li>If high priority processes take lots of CPU time, then the lower priority processes may starve and will be postponed for an indefinite time.</li>
                <li>This scheduling algorithm may leave some low priority processes waiting indefinitely.</li>
                <li>A process will be blocked when it is ready to run but has to wait for the CPU because some other process is running currently.</li>
                <li>If a new higher priority process keeps on coming in the ready queue, then the process which is in the waiting state may need to wait for a long duration of time.</li>
                <li>If the system eventually crashes, all low priority processes get lost.</li>
            </ul>
            <li><h3>Example</h3></li>
             <img src="https://github.com/NidhayPancholi/Scheduling-algo-simulator/blob/main/PRIORITYsCHEDULING.jpg">
            <li><h3>Implmentation</h3></li>
             <ol>
                 <li>First input the processes with their burst time and priority.</li>
                 <li>Sort the processes, burst time and priority according to the priority.</li>
                 <li>Now simply apply FCFS/RR algorithm.</li>
             </ol>
        </ul>    
    </li>
    
</ol>

