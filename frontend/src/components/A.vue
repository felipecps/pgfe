<template>
    <div>
        <p>
            {{texto}}
        </p>
    </div>
</template>
<script>
    export default {
        name: "A",
        props: {
            texto: { type: String }
        }
    }
</script>
