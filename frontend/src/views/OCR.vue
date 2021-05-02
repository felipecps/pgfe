<template>
    <div class="container">
        <div class="mb-3">
            <p>
                <h4>
                    Página para extração de texto de arquivos de imagem.
                </h4>
            </p>
        </div>
        <!-- Styled -->
        <b-form-file v-model="file1"
                     :state="Boolean(file1)"
                     placeholder="Escolha um arquivo ou arraste aqui..."
                     drop-placeholder="Arraste aqui..."></b-form-file>
        <div class="mt-3">Arquivo selecionado: {{ file1 ? file1.name : '' }}</div>

        <!-- Plain mode -->
        <b-form-file v-model="file2" class="mt-3" plain></b-form-file>
        <div class="mt-3">Arquivo selecionado: {{ file2 ? file2.name : '' }}</div>

        <div class="mt-3">
            <p>
                <h4>
                    {{ texto }}
                </h4>
            </p>
        </div>

    </div>
</template>

<script>
  export default {
    data() {
      return {
          texto: "Nenhum texto extraido ainda",
        file1: null,
        file2: null
      }
    }
  }
</script>