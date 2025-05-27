// Garante que o script só será executado após o HTML estar completamente carregado.
document.addEventListener('DOMContentLoaded', function () {

    // 1. Pegar referências aos elementos do HTML
    const codOperadorInput = document.getElementById('codOperador');
    const codEquipamentoInput = document.getElementById('codEquipamento');
    const btnLogin = document.getElementById('btnLogin');
    const btnTerminal = document.getElementById('btnTerminal');
    const btnAdmin = document.getElementById('btnAdmin');

    // Elementos do cabeçalho (para exibir informações)
    const headerInfoDiv = document.getElementById('headerInfo');
    const infoOperadorSpan = document.getElementById('infoOperador');
    const infoEquipamentoSpan = document.getElementById('infoEquipamento');

    // URL base da sua API (ajuste se for diferente)
    // Como o frontend está no Django, podemos usar caminhos relativos
    // se a API estiver no mesmo domínio.
    const API_BASE_URL = 'http://127.0.0.1:8000/api'; // Exemplo: http://127.0.0.1:8000/api

    // -----------------------------------------------------------------
    // Lógica para o Botão LOGIN
    // -----------------------------------------------------------------
    btnLogin.addEventListener('click', async function () {
        const codOperador = codOperadorInput.value.trim();
        const codEquipamento = codEquipamentoInput.value.trim();

        let operadorData = null;
        let equipamentoData = null;

        // Limpa o cabeçalho de informações anteriores
        infoOperadorSpan.textContent = '';
        infoEquipamentoSpan.textContent = '';
        headerInfoDiv.style.display = 'none';

        try {
            // Lógica: Se operador e equipamento preenchidos
            if (codOperador && codEquipamento) {
                console.log("Ambos os campos preenchidos. Buscando dados...");

                // GET /api/operador/{codigo}
                const responseOperador = await fetch(`${API_BASE_URL}/operador/${codOperador}/`);
                if (!responseOperador.ok) {
                    // Trata o erro se o operador não for encontrado ou outra falha na API
                    const erroOperador = await responseOperador.json();
                    alert(`Erro ao buscar operador: ${erroOperador.detail || responseOperador.statusText}`);
                    throw new Error(`Falha ao buscar operador: ${responseOperador.statusText}`);
                }
                operadorData = await responseOperador.json(); // Espera-se que retorne { "nome": "Nome do Operador" }

                // GET /api/equipamento/{codigo}
                const responseEquipamento = await fetch(`${API_BASE_URL}/equipamento/${codEquipamento}/`);
                if (!responseEquipamento.ok) {
                    const erroEquip = await responseEquipamento.json();
                    alert(`Erro ao buscar equipamento: ${erroEquip.detail || responseEquipamento.statusText}`);
                    throw new Error(`Falha ao buscar equipamento: ${responseEquipamento.statusText}`);
                }
                equipamentoData = await responseEquipamento.json(); // Espera-se que retorne { "nome": "Nome do Equipamento" }

                // Salvar os nomes e códigos em estado global (usando sessionStorage)
                sessionStorage.setItem('operadorCodigo', codOperador);
                sessionStorage.setItem('operadorNome', operadorData.nome);
                sessionStorage.setItem('equipamentoCodigo', codEquipamento);
                sessionStorage.setItem('equipamentoNome', equipamentoData.descequipamento);
                sessionStorage.setItem('modoOperacao', 'operacional');


                console.log("Operador:", operadorData.nome, "Equipamento:", equipamentoData.descequipamento);
                alert(`Login bem-sucedido!\nOperador: ${operadorData.nome}\nEquipamento: ${equipamentoData.descequipamento}`);

                // Exibir nomes no cabeçalho (simulação, pois vamos redirecionar)
                infoOperadorSpan.textContent = `Operador: ${operadorData.nome}`;
                infoEquipamentoSpan.textContent = `Equipamento: ${equipamentoData.descequipamento}`;
                headerInfoDiv.style.display = 'block';

                // Ir para a tela principal (modo operacional)
                // Substitua '/tela-principal/' pela URL correta da sua tela principal no Django
                window.location.href = '/app/tela-principal/'; // Exemplo de URL

            }
            // Lógica: Se apenas um estiver preenchido
            else if (codOperador || codEquipamento) {
                if (codOperador) {
                    console.log("Apenas operador preenchido. Buscando dados do operador...");
                    const responseOperador = await fetch(`${API_BASE_URL}/operador/${codOperador}/`);
                    if (!responseOperador.ok) {
                        const erroOperador = await responseOperador.json();
                        alert(`Erro ao buscar operador: ${erroOperador.detail || responseOperador.statusText}`);
                        throw new Error(`Falha ao buscar operador: ${responseOperador.statusText}`);
                    }
                    operadorData = await responseOperador.json();

                    sessionStorage.setItem('operadorCodigo', codOperador);
                    sessionStorage.setItem('operadorNome', operadorData.nome);
                    sessionStorage.removeItem('equipamentoCodigo'); // Garante que não há lixo
                    sessionStorage.removeItem('equipamentoNome');
                    sessionStorage.setItem('modoOperacao', 'parcial_operador');


                    alert(`Operador ${operadorData.nome} identificado. Código do equipamento será solicitado ao abrir uma ordem.`);
                    // Exibir nome no cabeçalho
                    infoOperadorSpan.textContent = `Operador: ${operadorData.nome}`;
                    infoEquipamentoSpan.textContent = `Equipamento: (Pendente)`;
                    headerInfoDiv.style.display = 'block';
                    // Normalmente, iria para a tela principal, e a lógica de pedir o equipamento
                    // ficaria lá, ao tentar abrir uma ordem.
                    window.location.href = '/app/tela-principal/'; // Exemplo

                } else { // Apenas equipamento preenchido
                    console.log("Apenas equipamento preenchido. Buscando dados do equipamento...");
                    const responseEquipamento = await fetch(`${API_BASE_URL}/equipamento/${codEquipamento}/`);
                    if (!responseEquipamento.ok) {
                        const erroEquip = await responseEquipamento.json();
                        alert(`Erro ao buscar equipamento: ${erroEquip.detail || responseEquipamento.statusText}`);
                        throw new Error(`Falha ao buscar equipamento: ${responseEquipamento.statusText}`);
                    }
                    equipamentoData = await responseEquipamento.json();

                    sessionStorage.setItem('equipamentoCodigo', codEquipamento);
                    sessionStorage.setItem('equipamentoNome', equipamentoData.descequipamento);
                    sessionStorage.removeItem('operadorCodigo'); // Garante que não há lixo
                    sessionStorage.removeItem('operadorNome');
                    sessionStorage.setItem('modoOperacao', 'parcial_equipamento');

                    alert(`Equipamento ${equipamentoData.descequipamento} identificado. Código do operador será solicitado ao abrir uma ordem.`);
                    // Exibir nome no cabeçalho
                    infoOperadorSpan.textContent = `Operador: (Pendente)`;
                    infoEquipamentoSpan.textContent = `Equipamento: ${equipamentoData.descequipamento}`;
                    headerInfoDiv.style.display = 'block';
                    window.location.href = '/app/tela-principal/'; // Exemplo
                }
            }
            // Lógica: Se nenhum preenchido
            else {
                alert("Por favor, preencha o código do operador e/ou do equipamento, ou entre como Terminal/Administrador.");
                console.log("Nenhum campo preenchido para login operacional.");
            }

        } catch (error) {
            console.error("Ocorreu um erro no login:", error);
            // Não redireciona, permite ao usuário tentar novamente.
        }
    });

    // -----------------------------------------------------------------
    // Lógica para o Botão TERMINAL (a ser implementada)
    // -----------------------------------------------------------------
    btnTerminal.addEventListener('click', function () {
        console.log("Botão Terminal clicado");
        sessionStorage.clear(); // Limpa qualquer login anterior
        sessionStorage.setItem('modoOperacao', 'terminal');
        sessionStorage.setItem('terminalNome', 'Terminal'); // Nome para exibição

        alert("Entrando em modo Terminal.");

        // Atualiza o cabeçalho (simulação)
        infoOperadorSpan.textContent = 'Modo: Terminal';
        infoEquipamentoSpan.textContent = ''; // Limpa o campo de equipamento
        headerInfoDiv.style.display = 'block';

        // Ir para a tela principal (modo terminal)
        // Substitua '/tela-principal/' pela URL correta
        window.location.href = '/app/tela-principal/'; // Exemplo de URL
    });

    // -----------------------------------------------------------------
    // Lógica para o Botão ADMINISTRADOR (a ser implementada)
    // -----------------------------------------------------------------
    btnAdmin.addEventListener('click', function () {
        console.log("Botão Administrador clicado");
        // Não limpa sessionStorage ainda, pois pode haver um login de admin
        // Redirecionar para a tela de login do administrador
        // Substitua '/admin/login/' pela URL correta da sua tela de login de admin no Django
        window.location.href = '/app/admin/login/'; // Exemplo de URL para login de admin
    });

});