<script>
    export let height;
    export let width;
    export let xScale;

    let start = 1990;
let end = 2024;
let specialTicks = [1990, 2000, 2010, 2020];
let xTicks = [];

for (let i = start; i <= end; i++) {
    xTicks.push(i);
}
  </script>
  
  <g class="axis x" >
    {#each xTicks as tick, index}
      <g class='tick' transform="translate({xScale(tick)}, 0)">
        <line x1={0} x2={0} y1={12} y2={18} stroke="hsla(212, 10%, 53%, 1)" />
        {#if specialTicks.includes(tick)}
        <text y={0} dy={6} text-anchor="middle" dominant-baseline="middle">{tick}s</text>
      {/if}
      </g>
    {/each}
    <text class="axis-title" 
          y={-9} 
          x={width} 
          text-anchor="end"
      >Year &rarr;</text
    >
  </g>