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
    x=0
    y={yScale(brand)}
    height={brand=="Alexander McQueen"? "20":"10"}
    />
    <text  x=5
    y={yScale(brand)}>{brand}</text>
  </g>
  {/each}
  </g>