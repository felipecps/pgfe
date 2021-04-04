<template>
    <div>
        <b-alert class="mt-3" v-if="mostra_resposta" show>{{ resposta }}</b-alert>
    </div>
</template>

<script>
    export default {
        props: {
            resposta: { type: String, required: true },
            mostra_resposta: { type: Boolean, required: true }
        }
    }
</script>