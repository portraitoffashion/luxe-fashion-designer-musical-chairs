<script>
    export let width;
    export let yScale;
    export let logoData;
console.log(logoData)
  </script>
  
  <g class='axis y'>
  {#each logoData as {brand, logo}}
  <g class='tick' transform="translate(0, {yScale(brand)})">
    <image
    href={logo}
    x=5
    y={yScale(brand)}
    width="30"
    height="30"
    />
  </g>
  {/each}
  </g>