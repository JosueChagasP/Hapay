import os
import json
import re
from pathlib import Path

def generate_habbo_figuremap():
    """
    Gera FigureMap.json completo baseado nos arquivos .nitro encontrados
    """
    
    # Caminho para pasta dos arquivos .nitro
    figure_path = r"C:\xampp\htdocs\assets\bundled\figure"
    
    # Verificar se pasta existe
    if not os.path.exists(figure_path):
        print(f"❌ ERRO: Pasta não encontrada: {figure_path}")
        print("📁 Verifique se o caminho está correto!")
        return
    
    print(f"🔍 Escaneando arquivos em: {figure_path}")
    
    # Mapear tipos de arquivo para códigos Habbo
    file_types = {
        'hair_': 'hr',      # Cabelos
        'head_': 'hd',      # Cabeças  
        'shirt_': 'ch',     # Camisas
        'shoes_': 'sh',     # Sapatos
        'trousers_': 'lg',  # Pernas/Calças
        'hat_': 'ha',       # Chapéus
        'jacket_': 'cc',    # Jaquetas
        'acc_': 'fa'        # Acessórios
    }
    
    # Estrutura do FigureMap
    figure_map = {
        "libraries": [],
        "aliases": {}
    }
    
    # Contar arquivos por tipo
    file_counts = {}
    
    # Escanear todos arquivos .nitro
    nitro_files = list(Path(figure_path).glob("*.nitro"))
    print(f"📊 Total de arquivos .nitro encontrados: {len(nitro_files)}")
    
    # Categorizar arquivos
    categorized_files = {}
    
    for file_path in nitro_files:
        filename = file_path.name
        
        # Determinar categoria do arquivo
        category = None
        for prefix, code in file_types.items():
            if filename.startswith(prefix):
                category = prefix
                break
        
        if category:
            if category not in categorized_files:
                categorized_files[category] = []
            categorized_files[category].append(filename)
    
    # Gerar mapeamentos
    current_id = 1
    
    for prefix, files in categorized_files.items():
        habbo_code = file_types[prefix]
        file_counts[prefix] = len(files)
        
        print(f"📋 {prefix}: {len(files)} arquivos → Códigos {habbo_code}-{current_id} até {habbo_code}-{current_id + len(files) - 1}")
        
        for i, filename in enumerate(files):
            # Remover extensão .nitro
            lib_name = filename.replace('.nitro', '')
            
            # ID numérico para este arquivo
            numeric_id = current_id + i
            
            # Determinar parts baseado no tipo
            parts = []
            
            if habbo_code == 'hr':  # Cabelos
                parts = [{"id": numeric_id, "type": "hr"}]
            elif habbo_code == 'hd':  # Cabeças
                parts = [{"id": numeric_id, "type": "hd"}]
            elif habbo_code == 'ch':  # Camisas
                parts = [
                    {"id": numeric_id, "type": "ch"},
                    {"id": numeric_id, "type": "ls"},
                    {"id": numeric_id, "type": "rs"}
                ]
            elif habbo_code == 'lg':  # Pernas
                parts = [{"id": numeric_id, "type": "lg"}]
            elif habbo_code == 'sh':  # Sapatos
                parts = [{"id": numeric_id, "type": "sh"}]
            elif habbo_code == 'ha':  # Chapéus
                parts = [{"id": numeric_id, "type": "ha"}]
            elif habbo_code == 'cc':  # Jaquetas
                parts = [
                    {"id": numeric_id, "type": "cc"},
                    {"id": numeric_id, "type": "lc"}, 
                    {"id": numeric_id, "type": "rc"}
                ]
            elif habbo_code == 'fa':  # Acessórios
                parts = [{"id": numeric_id, "type": "fa"}]
            
            # Adicionar ao mapeamento
            library_entry = {
                "id": lib_name,
                "revision": 1,
                "parts": parts
            }
            
            figure_map["libraries"].append(library_entry)
        
        current_id += len(files)
    
    # Salvar FigureMap.json
    output_path = os.path.join(figure_path, "..", "..", "gamedata_BR", "FigureMap_NEW.json")
    
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(figure_map, f, indent=2, ensure_ascii=False)
        
        print(f"\n🎉 SUCESSO! FigureMap.json gerado!")
        print(f"📁 Arquivo salvo em: {output_path}")
        print(f"📊 Total de libraries criadas: {len(figure_map['libraries'])}")
        
        # Relatório detalhado
        print("\n📋 RELATÓRIO DETALHADO:")
        print("=" * 50)
        for prefix, count in file_counts.items():
            habbo_code = file_types[prefix]
            print(f"{prefix:<12} {count:>3} arquivos → {habbo_code}-1 até {habbo_code}-{count}")
        
        print("\n🔧 PRÓXIMOS PASSOS:")
        print("1. Faça backup do FigureMap.json atual")
        print("2. Substitua pelo FigureMap_NEW.json")
        print("3. Reinicie o servidor")
        print("4. Teste os avatares!")
        
    except Exception as e:
        print(f"❌ ERRO ao salvar arquivo: {e}")
        
        # Salvar na pasta atual como fallback
        fallback_path = "FigureMap_NEW.json"
        with open(fallback_path, 'w', encoding='utf-8') as f:
            json.dump(figure_map, f, indent=2, ensure_ascii=False)
        print(f"💾 Arquivo salvo em: {os.path.abspath(fallback_path)}")

if __name__ == "__main__":
    print("🎯 HABBO FIGUREMAP GENERATOR")
    print("=" * 40)
    generate_habbo_figuremap()
    print("\n✅ Script finalizado!")
    input("Pressione Enter para sair...")