import os
import json
from pathlib import Path

def generate_habbo_soundmap():
    """
    Gera SoundMap.json completo baseado nos arquivos de som encontrados
    """
    
    # Caminho para pasta dos arquivos de som
    sounds_path = r"C:\xampp\htdocs\assets\sounds"
    
    # Verificar se pasta existe
    if not os.path.exists(sounds_path):
        print(f"❌ ERRO: Pasta não encontrada: {sounds_path}")
        print("📁 Verifique se moveu os sons para a pasta correta!")
        return
    
    print(f"🔍 Escaneando sons em: {sounds_path}")
    
    # Estrutura do SoundMap
    sound_map = {
        "libraries": []
    }
    
    # Escanear todos arquivos de som
    sound_files = []
    
    # Suportar múltiplos formatos
    sound_extensions = ['.mp3', '.ogg', '.wav', '.m4a']
    
    for ext in sound_extensions:
        files = list(Path(sounds_path).glob(f"*{ext}"))
        sound_files.extend(files)
    
    print(f"📊 Total de arquivos de som encontrados: {len(sound_files)}")
    
    if len(sound_files) == 0:
        print("❌ ERRO: Nenhum arquivo de som encontrado!")
        print("🔍 Verifique se os arquivos estão na pasta correta")
        return
    
    # Categorizar sons por nome (tentar identificar tipos)
    sound_categories = {
        'interface': [],
        'gameplay': [],
        'music': [],
        'effects': [],
        'other': []
    }
    
    # Palavras-chave para categorização
    interface_keywords = ['click', 'button', 'ui', 'menu', 'purchase', 'buy', 'credits', 'duckets']
    gameplay_keywords = ['walk', 'step', 'sit', 'stand', 'door', 'gate', 'teleport']
    music_keywords = ['music', 'song', 'melody', 'tune', 'track']
    effects_keywords = ['effect', 'sound', 'fx', 'ambient']
    
    # Gerar mapeamentos
    current_id = 1
    
    for sound_file in sound_files:
        filename = sound_file.name.lower()
        file_without_ext = sound_file.stem
        
        # Determinar categoria
        category = 'other'
        if any(keyword in filename for keyword in interface_keywords):
            category = 'interface'
        elif any(keyword in filename for keyword in gameplay_keywords):
            category = 'gameplay'
        elif any(keyword in filename for keyword in music_keywords):
            category = 'music'
        elif any(keyword in filename for keyword in effects_keywords):
            category = 'effects'
        
        sound_categories[category].append(sound_file.name)
        
        # Criar entrada no SoundMap
        library_entry = {
            "id": file_without_ext,
            "revision": 1,
            "parts": [
                {
                    "id": current_id,
                    "type": "sound"
                }
            ]
        }
        
        sound_map["libraries"].append(library_entry)
        current_id += 1
    
    # Salvar SoundMap.json
    output_path = os.path.join(sounds_path, "..", "gamedata_BR", "SoundMap_NEW.json")
    
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(sound_map, f, indent=2, ensure_ascii=False)
        
        print(f"\n🎉 SUCESSO! SoundMap.json gerado!")
        print(f"📁 Arquivo salvo em: {output_path}")
        print(f"📊 Total de sons mapeados: {len(sound_map['libraries'])}")
        
        # Relatório detalhado por categoria
        print("\n📋 RELATÓRIO DETALHADO:")
        print("=" * 50)
        
        for category, files in sound_categories.items():
            if files:
                print(f"{category.upper():<12} {len(files):>3} arquivos")
        
        # Mostrar alguns exemplos
        print("\n🎵 EXEMPLOS DE SONS MAPEADOS:")
        print("=" * 50)
        
        for i, library in enumerate(sound_map["libraries"][:10]):  # Primeiros 10
            sound_id = library["parts"][0]["id"]
            print(f"ID {sound_id:>3}: {library['id']}")
        
        if len(sound_map["libraries"]) > 10:
            print(f"... e mais {len(sound_map['libraries']) - 10} sons!")
        
        print("\n🔧 PRÓXIMOS PASSOS:")
        print("1. Faça backup do SoundMap.json atual (se existir)")
        print("2. Substitua/crie SoundMap.json pelo SoundMap_NEW.json")
        print("3. Reinicie o servidor Arcturus")
        print("4. Teste os sons no cliente!")
        
        # Criar também external_variables básico se não existir
        ext_vars_path = os.path.join(sounds_path, "..", "gamedata_BR", "external_variables.txt")
        
        if not os.path.exists(ext_vars_path):
            print("\n📝 CRIANDO external_variables.txt BÁSICO...")
            
            basic_variables = """# Habbo External Variables - Basic Sound Config
sound.enabled=true
sound.volume=0.8
sound.format=mp3
sound.path=/assets/sounds/
ui.sound.enabled=true
ui.sound.volume=0.6
"""
            
            try:
                with open(ext_vars_path, 'w', encoding='utf-8') as f:
                    f.write(basic_variables)
                print(f"✅ external_variables.txt criado em: {ext_vars_path}")
            except Exception as e:
                print(f"⚠️ Não foi possível criar external_variables.txt: {e}")
        
    except Exception as e:
        print(f"❌ ERRO ao salvar arquivo: {e}")
        
        # Salvar na pasta atual como fallback
        fallback_path = "SoundMap_NEW.json"
        with open(fallback_path, 'w', encoding='utf-8') as f:
            json.dump(sound_map, f, indent=2, ensure_ascii=False)
        print(f"💾 Arquivo salvo em: {os.path.abspath(fallback_path)}")

if __name__ == "__main__":
    print("🎵 HABBO SOUNDMAP GENERATOR")
    print("=" * 40)
    generate_habbo_soundmap()
    print("\n✅ Script finalizado!")
    input("Pressione Enter para sair...")