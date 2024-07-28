<script>
    export let currentStep1;
    import Scrolly from "../helpers/Scrolly.svelte";
    let intros=["The luxury fashion industry is a highly structured, hierarchical system, predominantly dominated by French and Italian brands.","Below, we explore some of the most prominent luxury fashion labels of our time, ranked by their estimated 2023 revenue","Despite the apparent diversity among these brands, many were acquired by major conglomerates throughout the 1980s and early 2000s. This acquisition spree formed a tiered matrix strategy that controls the supply chain, taste, and pricing across the entire industry."]
  </script>
  
  <div class="steps">
    <Scrolly bind:value={currentStep1}>
      {#each intros as text, i}
        <div class="step" class:active={currentStep1 === i}>
          <div class="step-content">
            <p>{text}</p>
          </div>
        </div>
      {/each}
    </Scrolly>
  </div>
  
  <style>
    .step {
      height: 90vh;
      opacity: 0.3;
      transition: opacity 300ms ease;
      display: flex;
      justify-content: center;
      place-items: center;
    }
  
    .step.active {
      opacity: 1;
    }
  
    .steps {
      z-index: 2;
      position: relative;
      pointer-events: none;
    }
  
    .step-content {
      padding: 0.75rem 1rem;
      border: 1px solid black;
      border-radius: 3px;
      background: white;
    }
  </style>