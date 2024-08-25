<script>
  import Intro from "$components/Intro.svelte";
   import Cover from "$components/Cover.svelte";
   import Hierarchy from "$components/Hierarchy.svelte";
  import Tooltip from "$components/Tooltip.svelte";
  import data from "$data/data.js";
  import logo from "$data/logo.js";
  import headshot from "$data/headshots.js";

  import { scaleLinear } from "d3-scale";
  import { scaleBand } from "d3-scale";
  import { max } from "d3-array";

  let logoData = logo.sort((a, b) => b.index - a.index);
  let headshotData = headshot.sort((a, b) => b.index - a.index);



let width = 800,
    height = 600;

  const margin = { top: 20, right: 100, bottom: 20, left: 100 };
  const radius = 10;
  

  $: innerWidth = width - margin.left - margin.right;
  $: innerHeight = height - margin.top - margin.bottom;

  $: xScale = scaleLinear()
    .domain([1990, 2024])
    .range([margin.left, innerWidth]);

  $: yScale = scaleBand()
    .domain(logo.map(d=>d.brand))
    .range([600,30]);

  let hoveredData;
  let hoveredData2;

  // Scrollytelling
  let currentStep1;
  let currentStep;

  let initialData = data.sort((a, b) => a.grade - b.grade);
  let renderedData = initialData;

  $: X_MIDPOINT = (xScale.domain()[0] + xScale.domain()[1]) / 2;
  $: Y_MIDPOINT = (yScale.domain()[0] + yScale.domain()[1]) / 2;

  $: {
    if (currentStep === 0) {
      renderedData = initialData.map(d => ({
        ...d,
        hours: Y_MIDPOINT,
        grade: X_MIDPOINT
      }));
      hoveredData = null;
    } else if (currentStep === 1) {
      renderedData = initialData.map(d => ({ ...d, hours: Y_MIDPOINT }));
      hoveredData = null;
    } else if (currentStep === 2) {
      renderedData = initialData;
      hoveredData = initialData[13];
    }
  }

  import SampleText from "$components/SampleText.svelte";
  import Chart from "$components/Chart.svelte";
  import Steps from "$components/Steps.svelte";
  import Steps1 from "$components/Steps1.svelte";
</script>

<main>

  <Cover />
  <Intro />
  <Hierarchy  
  {currentStep1}/>
 <Steps1 bind:currentStep1={currentStep1} />

  <h1>Students who studied longer scored higher on their final exams</h1>
  <SampleText />
  <section>
    <Chart
      {margin}
      {currentStep}
      {innerWidth}
      {innerHeight}
      {yScale}
      {xScale}
      {renderedData}
      {radius}
      {logoData}
      {headshotData}
      bind:width={width}
      bind:height={height}
      bind:hoveredData={hoveredData}
      bind:hoveredData2={hoveredData2}
    />
    <Steps bind:currentStep={currentStep} />
  </section>
  <SampleText />
  <SampleText />
</main>

<style>
  main {
    text-align: center;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    /* min-height: 100vh; */
    /* background: #f0f0f0; */
  }

  h1 {
    font-size: 3rem;
    margin-bottom: 1rem;
    font-weight: 700;
  }

  h2 {
    font-size: 1.5rem;
    color: #333;
    margin-bottom: 2rem;
    line-height: 1.5;
  }

  pre {
    padding: 1px 6px;
    display: inline;
    margin: 0;
    background: #ffb7a0;
    border-radius: 3px;
  }

  a {
    color: #ff3e00;
    text-decoration: inherit;
  }

  footer {
    font-size: 1rem;
    color: #333;
  }
</style>
