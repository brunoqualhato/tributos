import Foundation
import PDFKit
import Vision

guard CommandLine.arguments.count > 1 else {
    fputs("Uso: ocr_pdf <arquivo.pdf>\n", stderr)
    exit(1)
}

let caminho = CommandLine.arguments[1]
let url = URL(fileURLWithPath: caminho)

guard let doc = PDFDocument(url: url) else {
    fputs("Erro ao abrir PDF: \(caminho)\n", stderr)
    exit(2)
}

var textTotal: [String] = []

for i in 0..<doc.pageCount {
    guard let page = doc.page(at: i) else { continue }
    let pageBounds = page.bounds(for: .mediaBox)
    // Render at high resolution (2000 px width)
    let targetSize = CGSize(width: 2000, height: 2000 * (pageBounds.height / pageBounds.width))
    let img = page.thumbnail(of: targetSize, for: .mediaBox)
    guard let cgImage = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else { continue }
    
    let requestHandler = VNImageRequestHandler(cgImage: cgImage, options: [:])
    let request = VNRecognizeTextRequest()
    request.recognitionLevel = .accurate
    request.recognitionLanguages = ["pt-BR", "en-US"]
    request.usesLanguageCorrection = true
    
    do {
        try requestHandler.perform([request])
        guard let observations = request.results else { continue }
        let pageStrings = observations.compactMap { $0.topCandidates(1).first?.string }
        let pageText = pageStrings.joined(separator: "\n")
        if !pageText.isEmpty {
            textTotal.append("<!-- PÁGINA \(i + 1) -->\n" + pageText)
        }
    } catch {
        fputs("Erro no OCR da página \(i+1): \(error)\n", stderr)
    }
}

print(textTotal.joined(separator: "\n\n"))
