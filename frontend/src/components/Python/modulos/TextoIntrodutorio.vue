<template>
    <div>
        <p class="text-break">
            {{texto}}
        </p>
    </div>
</template>

<script>
    export default {
        props: {
            texto: { type: String, required: true }
        },
    }
</script>