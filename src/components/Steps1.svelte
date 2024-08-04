<script>
    export let currentStep1;
    import Scrolly from "../helpers/Scrolly.svelte";
    let intros=["The luxury fashion industry is a tapestry of structured hierarchy, dominated largely by iconic French and Italian brands. Let's delve into some of the most prominent players in this space, ranked in this pyramid graph by their estimated annual revenue.","Many of these illustrious brands began their journeys as small, independent ateliers. Over time, they have transformed into billion or even multi-billion dollar powerhouses.","Despite the apparent diversity, most of these brands have been swept up by major conglomerates like LVMH, Kering, and Richemont, especially during the acquisition waves of the 1980s and early 2000s. Out of the 18 designers highlighted, only four have maintained their independence.","These strategic acquisitions have crafted a matrixed approach that monopolizes nearly every facet of the market—from supply chains and talent acquisition to pricing strategies. Yet, even this seemingly invincible structure shows signs of strain."]
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
      width: 50%;
      margin: 0 auto;
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