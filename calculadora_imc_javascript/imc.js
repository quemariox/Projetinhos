// Pegando o botão calcular pelo id
const calcular = document.getElementById("calcular");

// Função que calcula o IMC
function imc() {
    // Pegando os valores dos campos de entrada pelo id
    const nome = document.getElementById("nome").value;
    const altura = parseFloat(document.getElementById("altura").value);
    const peso = parseFloat(document.getElementById("peso").value);
    const resultado = document.getElementById("resultado");

    // Validação do preenchimento dos campos
    if (nome !== "" && !isNaN(altura) && !isNaN(peso)) {
        // Calculando o IMC
        const valorIMC = (peso / (altura * altura)).toFixed(2);

        // Classificação do IMC
        let classificacao = '';

        if (valorIMC < 18.5) {
            classificacao = 'abaixo do peso';
        } else if (valorIMC < 25) {
            classificacao = 'com peso ideal, parabéns';
        } else if (valorIMC < 30) {
            classificacao = 'em sobrepeso';
        } else if (valorIMC < 35) {
            classificacao = 'com obesidade grau 1, cuidado';
        } else if (valorIMC < 40) {
            classificacao = 'com obesidade grau 2, muito cuidado';
        } else {
            classificacao = 'com obesidade grau 3, vá ao médico agora';
        }

        // Exibindo o resultado
        resultado.textContent = `${nome}, seu IMC é ${valorIMC} e você está ${classificacao}.`;
    } else {
        resultado.textContent = "Preencha todos os campos corretamente!";
    }
}

// Adicionando um evento de clique ao botão calcular para chamar a função IMC
calcular.addEventListener("click", imc);
