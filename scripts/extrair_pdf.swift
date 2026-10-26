import Foundation
import PDFKit

guard CommandLine.arguments.count > 1 else {
    fputs("Uso: extrair_pdf <arquivo.pdf>\n", stderr)
    exit(1)
}

let caminho = CommandLine.arguments[1]
let url = URL(fileURLWithPath: caminho)

guard let doc = PDFDocument(url: url) else {
    fputs("Erro ao abrir PDF: \(caminho)\n", stderr)
    exit(2)
}

var partes: [String] = []
for i in 0..<doc.pageCount {
    if let pagina = doc.page(at: i), let texto = pagina.string {
        let limpo = texto.trimmingCharacters(in: .whitespacesAndNewlines)
        if !limpo.isEmpty {
            partes.append(limpo)
        }
    }
}

print(partes.joined(separator: "\n\n"))
