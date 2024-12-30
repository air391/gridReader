
path := invocation_directory()
ksy_path := path / "src/gridreader/format/ksy"
ksy_output := path / "src/gridreader/format/"
default:
    @just --list
print:
    #!/usr/bin/env bash
    echo "{{path}}"
    echo "{{ksy_path}}"
clear_format:
    find {{ksy_output}} -maxdepth 1 -type f ! -name "__init__.py" -delete
compile_ksy:
    #!/usr/bin/env bash
    for file in $(find {{ksy_path}} -type f); do
        if [[ -f "$file" ]]; then
            filename=$(basename -- "$file")
            extension="${filename##*.}"
            name="${filename%.*}"

            if [[ "$extension" == "ksy" ]]; then
                # 调用 ksc 命令生成文件
                echo "Compiling $file to {{ksy_output}}"
                ksc -t python --python-package . --outdir {{ksy_output}} "$file"

                if [[ -f "{{ksy_output}}/frameseq.py" ]]; then
                    mv "{{ksy_output}}/frameseq.py" "{{ksy_output}}/${name}.py"
                fi
            fi
        fi
    done