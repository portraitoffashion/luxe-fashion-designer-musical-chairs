<script>
    export let width;
    export let yScale;
    export let xScale;
    export let logoData;
    let genderBrands=['Louis Vuitton Men','Louis Vuitton Women','Hermes Men','Hermes Women','Dior Men','Dior Women','Fendi Men','Fendi Women']
console.log(logoData)
  </script>
  
  <g class='axis y'>
  {#each logoData as {brand, logo}}

  <g class='tick' transform="translate(0, {yScale(brand)})">
    <line x1={xScale(1990)} x2={width} y1={yScale(brand)+10} y2={yScale(brand)+10} stroke='#e5e7eb' /> 
    <image
    href={logo}
    x=-50
    y={yScale(brand)}
    height={brand == "Alexander McQueen" ? "24" :  (brand == "Maison Margiela" || brand == "Chloe")? "12":"10"}
    />
    {#if genderBrands.includes(brand)}
    <text  x=-50
    y={yScale(brand)+25}>{brand.split(" ").slice(-1)}</text>
    {/if}
  </g>
  {/each}
  </g>