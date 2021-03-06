This is an overview of major changes. Refer to the git repository for a full log change.

Version 0.1.6
-------------
- Workaround for broken barcode reading on Windows (#130) (@quicklizard)
- Metadata fields are Simple Darwin Core terms (#116) (@quicklizard)
- Improved test coverage (#84) - (@quicklizard)
- Fixed #127 - .tif file extension not recognised (@quicklizard)
- Fixed #125 - Display issue on Windows: After startup, Window title, frame and controls out of screen (@quicklizard)
- Fixed #124 - "New" doesn't work if inselect document already exists (@quicklizard)
- Fixed #119 Non-latin characters in 'Specimen number' metadata field causes grid item title to disappear (@quicklizard)
- Fixed #115 - Silly wording when a single box selected (@quicklizard)
- Fixed #106 - Select newly created bounding box (@quicklizard)
- Fixed #104 - File, Open versus File, New ambiguity (@quicklizard)
- Fixed #87 - Large images do not display correctly (@quicklizard)
- Fixed #74 - Mac OS X installer (@quicklizard)

Version 0.1.5
-------------
- Icons for plugins (@quicklizard)
- CSV export (@quicklizard)
- Progress box during 'New document' (@quicklizard)
- Open files via drag-drop (@quicklizard)

Version 0.1.4
-------------
- Document format (@quicklizard)
- Workflow tools (@quicklizard)
- UI reimplementation (@quicklizard)
- OS X (Mac) build (@quicklizard)
- Myriad bug fixes and enhancements (@quicklizard)
- Add license and changelog (@aliceh75)
- Added help dialog (@aliceh75)
- Add previous/next navigation in the annotation dialog (@aliceh75)
- Refactor code to separate UI and application logic (@aliceh75)
- Add padding option (@holtzhau)
- Improve segmentation by resizing image (@holtzhau)

Version 0.1.3
-------------
- Add persistent settings and settings dialog box (@aliceh75)
- Segmentation algorithm tweaks (@holtzhau)
- Added tiff image detection on export (@holtzhau)
- Make exported image name configurable via settings (@aliceh75)
- Refactor file structure to prepare for UI/application logic separation (@aliceh75)
- Refactor BoxResiable to use mouse events (@aliceh75)
- Fix box ordering on keyboar next/previous (@holtzhau)
- Remember open directory (@holtzhau)

Version 0.1.2
-------------
- Multiple object annotation (@holtzhau)
- Added key navigation to sidebar (@holtzhau)
- Various fixes (@holtzhau)

Version 0.1.1
-------------
- Added annotator dialog (@holtzhau)
- Switch from multiprocessing to QThreads (@holtzhau)
- Added display_image routine and elaborated on resegment (@holtzhau)
- Added sidebar (@holtzhau)
- Added importing and saving of boxes (@holtzhau)
- Use json for import/export (@holtzhau)
- Improvement to segmentation (@holtzhau)
- Added seed growing in segmentation and interface (@holtzhau)
- Key based navigation (@aliceh75)
- Refactor mouse event handling (@aliceh75)
- Add zoom with wheel (@aliceh75)

Version 0.1
-----------
- Initial test release (@stefanv, @holtzhau)
