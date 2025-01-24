from flask import Blueprint, render_template , request
from database.tarefas import TAREFAS

user_route = Blueprint('user', __name__)

"""""
    
        -/user/ (post) - inserir tarefa no servidor 
        -/user/ (GET) - renderizar formulario para criar tarefa
        -/user/<id> - (GET) - mostrar detalhes das tarefas
        -/user/<id>/edit (get) - renderizar formulario para alterar tarefa
        -/user/<id>/update (put) - atualizar os dados da tarefa 
        -/user/<id>/delet (delete) - deletar tarefa uma por uma
        - /user/<id>/delet (delete) - deletar todas tarefas

    """""

@user_route.route('/')
def listar_tarefas():
    return render_template('listar_tarefas.html' , tarefa=TAREFAS)

@user_route.route('/' , methods=['POST'])
def inserir_tarefa():
    data = request.json 

    nova_tarefa = {
          "id" : len(TAREFAS) + 1 ,
          "titulo" : data['titulo'],
          "descrição" : data['descrição'],
          "status" : data['status'],
    }

    TAREFAS.append(nova_tarefa)

    if nova_tarefa['status'] == 'INICIAR':
        return render_template('item_tarefa_iniciar.html', tarefa=nova_tarefa)
    
    elif nova_tarefa['status'] == 'INICIADA':
        return render_template('item_tarefa_iniciado.html', tarefa=nova_tarefa)
    else:
        return render_template('item_tarefa_finalizado.html', tarefa=nova_tarefa)

  

@user_route.route('/new')
def form_tarefa():
    
    return render_template('form_tarefa.html')

@user_route.route('/<int:tarefa_id>')
def detalhe_tarefa(tarefa_id):
    
    return render_template('detalhe_tarefa.html')


@user_route.route('/<int:tarefa_id>/edit')
def editar_tarefa(tarefa_id):
        return render_template('form_edit.html')


@user_route.route('/<int:tarefa_id>/update', methods=['PUT'])
def atualizar_tarefa(tarefa_id):
        pass  

@user_route.route('/<int:tarefa_id>/delete', methods=['DELETE'])
def deletar_tarefa(tarefa_id):
        pass  