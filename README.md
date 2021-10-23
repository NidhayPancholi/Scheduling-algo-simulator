<h1>Scheduling-algo-simulator</h1>

<p>
Scheduling algorithms decide in which order should the processes be scheduled on the CPU. The scheduling algorithms differe based on the factors which the use to decide the mext scheduled process. There are static and dynamic prediction algorithms. Let's have a look at these algorithms in details. 
</p>


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


