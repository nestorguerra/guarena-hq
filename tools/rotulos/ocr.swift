// The text in pictures, read by macOS's own OCR (Vision): swift tools/rotulos/ocr.swift a.jpg b.jpg … → one JSON line
// per picture: {"f": path, "t": ["line", …]} (backlog R-09: tools/rotulos/legibilidad.py)
import Foundation
import Vision
import AppKit

for path in CommandLine.arguments.dropFirst() {
    var lines: [String] = []
    if let img = NSImage(contentsOfFile: path), let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) {
        let req = VNRecognizeTextRequest()
        req.recognitionLevel = .accurate
        req.recognitionLanguages = ["es-ES"]
        req.usesLanguageCorrection = false
        req.minimumTextHeight = 0.01
        try? VNImageRequestHandler(cgImage: cg, options: [:]).perform([req])
        for o in req.results ?? [] { if let c = o.topCandidates(1).first { lines.append(c.string) } }
    }
    let d = try! JSONSerialization.data(withJSONObject: ["f": path, "t": lines])
    print(String(data: d, encoding: .utf8)!)
    fflush(stdout)
}
