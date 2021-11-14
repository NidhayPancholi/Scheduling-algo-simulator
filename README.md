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

<h2>Now the algorithms used here are:</h2>

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
        <h3><a href="https://www.geeksforgeeks.org/program-shortest-job-first-sjf-scheduling-set-1-non-preemptive/">SJF(Shortest Job First)</a></h3>
        <p></p>
    </li>
    <li>
        <h3><a href="https://www.geeksforgeeks.org/program-round-robin-scheduling-set-1/">Round Robin</a></h3>
        <p></p>
    </li>
    <li>
        <h3><a href="https://www.geeksforgeeks.org/program-priority-scheduling-set-1/">Priority Scheduling</a></h3>
        <p></p>
    </li>
    
</ol>

